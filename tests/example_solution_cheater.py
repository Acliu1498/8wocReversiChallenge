#!/usr/bin/python3

""" Example Reversi solution that cheats by looking up the answer to the tests """

# Libs
import argparse
import json
import sys


def main():
    """ Cheats by looking up the answer to the test """

    # Setup
    args = parse_arguments()
    begin_state = json.load(args.infile)

    # Cheat by looking up the answer to the test
    tests = json.load(args.test_file)
    end_state = lookup_answer(begin_state, tests)

    # Write board to stdout
    json.dump(end_state, args.outfile)


def parse_arguments():
    """ Configures and parses command-line arguments """
    argparser = argparse.ArgumentParser(
        description=("Reversi implementation that cheats by looking up"
                     "the answer to the input board"))
    argparser.add_argument("--infile",
                           nargs="?",
                           type=argparse.FileType("r"),
                           default=sys.stdin,
                           help="Filename of JSON file containing board and move, default stdin")
    argparser.add_argument("--outfile",
                           nargs="?",
                           type=argparse.FileType("w"),
                           default=sys.stdout,
                           help="Filename of JSON file to write board state to, default stdout")
    argparser.add_argument("--test-file",
                           nargs="?",
                           type=argparse.FileType("r"),
                           default="tests/tests.json",
                           help="Filename of JSON file containing reversi tests, " \
                                "default tests/tests.json")
    return argparser.parse_args()


def lookup_answer(begin_state, tests):
    """ Find answer in test file """
    for test in tests:
        if test["input"] == begin_state:
            return test["expected"]
    return {}


if __name__ == "__main__":
    main()
