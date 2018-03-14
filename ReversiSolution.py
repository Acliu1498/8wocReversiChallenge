
import json
import argparse
import sys


def main():
    """Returns a new board with the move having taken place"""

    # Gets input
    args = parse_arguments()
    begin_state = json.load(args.infile)

    # Gets the current board
    board = begin_state['board']

    # sets move equal to the given move input
    move = begin_state['move']
    make_move(move, board)

    end_state = {'board': board}

    # writes the board to the out
    json.dump(end_state, args.outfile, indent=4)


def make_move(move, board):
    """ this checks every direction from starting to see if a capture has been made"""

    # a map of how to check in each direction
    dir_map = {'U': -8, 'D': 8, 'L': -1, 'R': 1, 'DL': 7, 'DR': 9, 'UL': -7, 'UR': -9}

    # gets x and y from column and row
    x = move['column'] - 1
    y = move['row'] - 1

    # finds the starting index and places a piece there
    start = x + (8 * (y % 8))
    board[start] = move['player']

    # runs make_move_helper for every direction
    for key in dir_map:
        make_move_help(start, board, key, dir_map, start, move['player'])


def make_move_help(start, board, direction, dir_map, curr, player):
    """ Helper method for make_move that recurses in a given direction
    direction until the end of the board is reached, a player piece is reached
    or a 0 is reached"""

    # check if the current location is within the bounds and there is a piece at the current location
    if 0 <= curr < 64 and board[curr] != 0:
        # checks if the current spot is the player
        if board[curr] == player and curr != start:
            return True

        # moves according to the map
        curr += dir_map[direction]

        # makes a recursive call and checks if true
        if make_move_help(start, board, direction, dir_map, curr, player):
            # if true sets current value to player
            board[curr] = player
            return True

    return False


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
