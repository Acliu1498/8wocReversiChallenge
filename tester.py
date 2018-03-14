#!/usr/bin/python3

""" Tests an executable for correct reversi states """

# Libs
import argparse
import json
import subprocess
import sys


def main():
    """ Tests the given executable for correct reversi states """
    args = parse_arguments()
    tests = json.load(args.test_file)
    results = execute_tests(tests, args.executable)
    json.dump(results, args.outfile)
    for result in results:
        if not result["pass"]:
            sys.exit(1)


def parse_arguments():
    """ Configures and parses command-line arguments """
    argparser = argparse.ArgumentParser(
        description=("Test an executable for Reversi plays.  Prints "
                     "result file to outfile.  Exits with return code 1 "
                     "if any tests fail."))
    argparser.add_argument("--test-file",
                           nargs="?",
                           type=argparse.FileType("r"),
                           default="tests/tests.json",
                           help=("Filename of JSON file containing "
                                 "reversi tests, default tests.json"))
    argparser.add_argument("--outfile",
                           nargs="?",
                           type=argparse.FileType("w"),
                           default=sys.stdout,
                           help=("Filename of JSON test results, "
                                 "default stdout"))
    argparser.add_argument("executable",
                           help="Name of command line to invoke")
    return argparser.parse_args()


def execute_tests(tests, executable):
    """ Execute all tests """
    results = []
    for test in tests:
        result = execute_test(test, executable)
        results.append(result)
    return results


def execute_test(test, executable):
    """ Execute single test """
    result = {}
    stdin = json.dumps(test["input"])
    if sys.platform == 'win32':
        executable = ["python.exe", executable]
    stdout = subprocess.check_output(executable,
                                     input=stdin.encode("utf-8"))
    output = json.loads(stdout.decode("utf-8"))
    if output == test["expected"]:
        result["pass"] = True
    else:
        result["pass"] = False
        result["input"] = test["input"]
        result["expected"] = test["expected"]
        result["actual"] = output
    return result


if __name__ == "__main__":
    main()
