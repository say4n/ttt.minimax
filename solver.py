from ttt import TicTacToe
from copy import deepcopy as dc

def minimax(game, is_maximizing):
    if game.is_gameover():
        return game.get_reward()

    if is_maximizing:
        max_value = float("-inf")

        for move in game.get_empty_cells():
            game_t = dc(game)
            game_t.act(move)
            value = minimax(game_t, False)
            del game_t
            max_value = max(max_value, value)

        return max_value
    else:
        min_value = float("inf")

        for move in game.get_empty_cells():
            game_t = dc(game)
            game_t.act(move)
            value = minimax(game_t, True)
            del game_t
            min_value = min(min_value, value)

        return min_value

def player_move():
    game.step()

def computer_move():
    best_move, best_value = None, float("-inf")
    for move in game.get_empty_cells():
        game_t = dc(game)
        game_t.act(move)
        value = minimax(game_t, False)

        if value > best_value:
            best_value = value
            best_move = move

    game.act(best_move)

if __name__ == "__main__":
    game = TicTacToe()

    choice = input("Do you want to first (y/Y)? ")
    go_first = choice == "y" or choice == "Y"


    while not game.is_gameover():
        if go_first:
            if game.get_turn() == 1:
                player_move()
            else:
                computer_move()
        else:
            if game.get_turn() == 1:
                computer_move()
            else:
                player_move()

    if game.winner == "TIE":
        print("TIE!")