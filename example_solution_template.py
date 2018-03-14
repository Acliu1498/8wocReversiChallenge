#!/usr/bin/python3

""" Example Reversi implementation that reads a JSON board and move from
    stdin and writes a JSON board to stdout. """

# Libs
import argparse
import json
import sys


def main():
    """ Naively returns the same board it was given """

    # Read input
    args = parse_arguments()
    begin_state = json.load(args.infile)


    # Naively copy the input board
    # TODO: Implement move and put the resulting board into end_state
    end_state = {}
    end_state["board"] = begin_state["board"]

    # Write board to stdout
    json.dump(end_state, args.outfile)


def parse_arguments():
    """ Configures and parses command-line arguments """
    argparser = argparse.ArgumentParser(
        description="Naive Reversi implementation")
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
    return argparser.parse_args()


if __name__ == "__main__":
    main()
