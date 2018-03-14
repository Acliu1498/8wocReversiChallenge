
import json
import argparse
import sys


def main():
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
    json.dump(end_state, args.outfile)


def make_move(move, board):
    """ this checks every direction from starting to see if a capture has been made"""

    # dictionary of directions
    directions = {1: 'U', 2: 'D', 3: 'L', 4: 'R'}

    # gets x and y from column and row
    x = move['column'] - 1
    y = move['row'] - 1
    # runs make_move_helper for every direction
    start = x + (8 * (y % 8))
    board[start] = move['player']
    for key in directions:
        make_move_help(start, board, directions[key], start, move['player'])


def make_move_help(start, board, direction, curr, player):
    """ Helper method for make_move that recurses in a certain
    direction until the end of the board is reached, a player piece is reached
    or a 0 is reached"""

    # check if the current location is within the bounds and there is a piece at the current location
    if 0 <= curr < 64 and board[curr] != 0:
        # checks if the current spot is the player
        if board[curr] == player and curr != start:
            return True

        # if U moves up elif D moves down elif L moves left else moves right
        if direction == 'U':
            curr -= 8
        elif direction == 'D':
            curr += 8
        elif direction == 'L':
            if curr % 8 == 0:
                return False
            curr -= 1
        else:
            if curr % 8 == 7:
                return False
            curr += 1

        # makes a recursive call and checks if true
        if make_move_help(start, board, direction, curr, player):
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