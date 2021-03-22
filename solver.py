from ttt import TicTacToe
from copy import deepcopy as dc

def minimax(game, is_maximizing):
    if game.is_gameover():
        print(game)
        return game.get_reward()

    if is_maximizing:
        max_value = float("-inf")

        for move in game.get_empty_cells():
            game_t = dc(game)
            game_t.act(move)
            value = minimax(game_t, False)
            max_value = max(max_value, value)

        return max_value
    else:
        min_value = float("inf")

        for move in game.get_empty_cells():
            game_t = dc(game)
            game_t.act(move)
            value = minimax(game_t, True)
            min_value = min(min_value, value)

        return min_value

if __name__ == "__main__":
    game = TicTacToe()

    while not game.is_gameover():
        # Turn for player.
        if game.get_turn() == 1:
            game.step()
        # Turn for computer.
        else:
            best_move, best_value = None, float("-inf")
            for move in game.get_empty_cells():
                game_t = dc(game)
                game_t.act(move)
                value = minimax(game_t, False)

                if value > best_value:
                    best_value = value
                    best_move = move

            game.act(best_move)
