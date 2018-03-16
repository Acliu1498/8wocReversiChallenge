import pygame
import json
import argparse
import sys
import copy
import ReversiSolution as sol

class reversi:

    def __init__(self, args):
        pygame.init()
        self.screen = pygame.display.set_mode((810, 810))
        self.font = pygame.font.SysFont('Comic Sans MS', 48)
        self.currPlayer = 1
        begin_state = json.load(args.infile)
        self.board = begin_state['board']
        self.notice = "Player 1 goes first!"
        self.winner = ""

        play = True
        while play:
            self.draw()
            for event in pygame.event.get():
                # exit if user tries to exit
                if event.type == pygame.QUIT:
                    play = False
                elif event.type == pygame.KEYDOWN:
                    # allows user to close out
                    if event.key == pygame.K_n or event.key == pygame.K_ESCAPE:
                        play = False
                if not self.winner:
                    if event.type == pygame.MOUSEBUTTONUP:
                        # if the user clicks check the move and change player if true
                        if not self.check():
                            self.notice = "You cannot move there"
                        else:
                            self.currPlayer = 1 if self.currPlayer == 2 else 2
                            self.notice = "Player " + str(self.currPlayer) + "'s Turn"
                else:
                    if event.type == pygame.K_y:
                        self.board = json.load(args.infile)
                        self.draw()
                        self.winner = ""
                    elif event.type == pygame.K_n:
                        play = False

    def check(self):
        """Helper method to check if a move is legal, if so makes move"""
        pos = pygame.mouse.get_pos()
        # changes actual xy to 2d array xy
        x = int(pos[0] / 100)
        y = int(pos[1] / 100)

        # makes a deep copy of board to be mutated
        new_board = copy.deepcopy(self.board)
        sol.make_move({'player': self.currPlayer, 'row': y + 1, 'column': x + 1}, new_board)

        # calculates number of differences
        diff = 0
        for i in range(len(self.board)):
            if self.board[i] != new_board[i]:
                diff += 1

        # if differences greater then one then legal move
        if diff > 1:
            # sets the old board = to the new board and returns true
            self.board = new_board
            self.draw()
            self.notice = ""
            self.end_game()
            return True
        return False

    def draw(self):
        """ Helper method to draw the current state of the board """
        # start of the board rectangle
        start = 0
        self.screen.fill([34, 139, 34])

        # while we haven't reached the end of the board add rectangles
        while start < 810:
            pygame.draw.rect(self.screen, (0, 0, 0), (start, 0, 10, 800))
            pygame.draw.rect(self.screen, (0, 0, 0), (0, start, 800, 10))
            start += 100

        # adds the pieces to their respective spots
        for i in range(len(self.board)):
            # the actual x and y values
            x = int(((i % 8) * 100) + 50)
            y = int(((int(i / 8)) * 100) + 50)

            # if 1 draws a white circle else if 2 draw a black circle
            if self.board[i] == 1:
                pygame.draw.circle(self.screen, (0, 0, 0), (x, y), 40)
            if self.board[i] == 2:
                pygame.draw.circle(self.screen, (255, 255, 255), (x, y), 40)

        text_surface = self.font.render(self.notice, False, (255, 255, 255))

        self.screen.blit(text_surface, (400 - (text_surface.get_rect().width / 2), 100))
        # Update Pygame display.
        pygame.display.flip()

    def end_game(self):
        """Checks if the game is over and if so says who the winner is"""
        # the current player being examined
        player1 = 0
        player2 = 0
        # goes through the board checking to see if it is full
        for i in range(len(self.board)):
            if self.board[i] == 0:
                return ""
            if self.board[i] == 1:
                player1 += 1
            else:
                player2 += 2
        if player1 > player2:
            # if player 1's pieces are greater than 2s p1 wins
            self.notice = 'Player 1 wins \n'
            self.winner = player1
        elif player2 > player1:
            # else if player 2's pieces are greater than 1s p2 wins
            self.notice = 'Player 2 wins \n'
            self.winner = player2
        else:
            # else its a draw
            self.notice = 'Draw \n'
            self.winner = 'draw'

        # asks user to play again
        self.notice += 'Play Again? (Y/N)'
        self.draw()


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
    args = parse_arguments()
    visual = reversi(args)