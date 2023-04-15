from engine import greeting, game
from texts import mode_dict, choose_game_mode, error_no_game_mode, value_error


def main():
    greeting()
    for k, v in mode_dict.items():
        print(f'{k}. {v[0]}')
    while True:
        try:
            game_mode = int(input(choose_game_mode))
            if game_mode in mode_dict.keys():
                game(game_mode)
            else:
                print(error_no_game_mode)
        except ValueError:
            print(value_error)


main()
