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

        self.gameover = False
        self.winner = None

    def act(self, cell):
        # Set value of cell to player's mark.
        self.board[cell] = self.player_lut[self.player]
        # Change turn of player.
        self.player ^= 1
        # Check if game has been won.
        self.__check_win()

    def get_empty_cells(self):
        return [index for index, val in enumerate(self.board) if val is None]

    def is_gameover(self):
        return self.gameover

    def get_turn(self):
        return self.player

    def get_reward(self):
        # Computer wins.
        if self.winner == "O":
            return 1
        # Player wins.
        elif self.winner == "X":
            return -1
        # It is a draw.
        else:
            return 0

    def __check_win(self):
        # Check rows.
        for offset in range(3):
            if self.board[offset * 3] == self.board[1 + offset * 3] and\
                    self.board[1 + offset * 3] == self.board[2 + offset * 3] and\
                    self.board[offset * 3] is not None:

                self.gameover = True
                self.winner = self.board[offset * 3]
                return self.board[offset * 3]

        # Check columns.
        for offset in range(3):
            if self.board[offset] == self.board[3 + offset] and\
                self.board[3 + offset] == self.board[6 + offset] and\
                self.board[offset] is not None:

                self.gameover = True
                self.winner = self.board[offset]
                return self.board[offset]

        # Check diagonal.
        if self.board[0] == self.board[4] and self.board[4] == self.board[8] and\
            self.board[0] is not None:

            self.gameover = True
            self.winner = self.board[0]
            return self.board[0]

        # Check alternate diagonal.
        if self.board[2] == self.board[4] and self.board[4] == self.board[6] and\
            self.board[2] is not None:

            self.gameover = True
            self.winner = self.board[2]
            return self.board[2]

        # Check for draw.
        if len(self.get_empty_cells()) == 0:
            self.gameover = True
            self.winner = "TIE"

            return None

        return None

    def step(self):
        print(f"Player {self.player_lut[self.get_turn()]}'s turn.")
        print(self)
        free_cells = self.get_empty_cells()
        print("Avalabible moves are: ", free_cells)
        choice = int(input("Select your move > "))

        if choice not in free_cells:
            raise ValueError(f"'{choice}' is not a valid move.")

        self.act(choice)

    def play(self):
        while not self.is_gameover():
            self.step()

        win = self.__check_win()
        if win is not None:
            print(f"{win} won!")
        else:
            print("TIE")

    def __repr__(self):
        to_print = ""

        for row in range(3):
            for col in range(3):
                # Row major index.
                index = 3 * row + col

                if self.board[index] is None:
                    if col == 1:
                        to_print += f" | {index} | "
                    else:
                        to_print += f"{index}"
                else:
                    if col == 1:
                        to_print += f" | {self.board[index]} | "
                    else:
                        to_print += f"{self.board[index]}"

            if row < 2:
                to_print += "\n" + "-" * 9 + "\n"
            else:
                to_print += "\n"

        return to_print


if __name__ == "__main__":
    game = TicTacToe()
    game.play()