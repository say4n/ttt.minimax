"""
Tic Tac Toe game implementation.
"""

class TicTacToe:
    def __init__(self):
        self.board = [None] * 9
        self.player = 1

        self.player_lut = {
            0: "O",
            1: "X"
        }

    def act(self, player):
        return player ^ 1

    def get_empty_cells(self):
        pass

    def __check_win(self):
        # Check rows.
        for offset in range(3):
            if self.board[offset * 3] == self.board[1 + offset * 3] and\
                    self.board[1 + offset * 3] == self.board[2 + offset * 3] and\
                    self.board[offset * 3] is not None:

                return self.board[offset * 3]

        # Check columns.
        for offset in range(3):
            if self.board[offset] == self.board[3 + offset] and\
                self.board[3 + offset] == self.board[6 + offset] and\
                self.board[offset] is not None:

                return self.board[offset]

        # Check diagonal.
        if self.board[0] == self.board[4] and self.board[4] == self.board[8] and\
            self.board[0] is not None:

            return self.board[0]

        # Check alternate diagonal.
        if self.board[2] == self.board[4] and self.board[4] == self.board[6] and\
            self.board[2] is not None:

            return self.board[2]


    def __repr__(self):
        pass
