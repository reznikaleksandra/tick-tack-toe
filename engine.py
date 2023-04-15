import random

from texts import greeting_text, cell_not_free_text, text_winner_player, text_winner_computer, text_winner_x, \
    text_winner_o, text_winner_both, move_x, move_o, move_computer, error_board_dict

board_dict = {1: '-', 2: '-', 3: '-', 4: '-', 5: '-', 6: '-', 7: '-', 8: '-', 9: '-'}
current_player = None


def board():
    print(board_dict[1], board_dict[2], board_dict[3])
    print(board_dict[4], board_dict[5], board_dict[6])
    print(board_dict[7], board_dict[8], board_dict[9])


def greeting():
    print(greeting_text)


def is_board_full():
    if '-' in board_dict.values():
        return True
    else:
        return False


def check_cell(cell):
    if board_dict[cell] != '-':
        return True
    else:
        return False


def move(player):
    global current_player
    current_player = player
    while True:
        try:
            if player == 'x':
                i = int(input(move_x))
                if i in board_dict.keys():
                    if check_cell(i):
                        print(cell_not_free_text)
                    else:
                        board_dict[i] = player
                        break
                else:
                    print(error_board_dict)
            elif player == 'o':
                i = int(input(move_o))
                if i in board_dict.keys():
                    if check_cell(i):
                        print(cell_not_free_text)
                    else:
                        board_dict[i] = player
                        break
                else:
                    print(error_board_dict)
        except ValueError:
            print(error_board_dict)


def computer_move(player):
    global current_player
    current_player = player
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while True:
        i = random.choice(a)
        if check_cell(i):
            continue
        else:
            print(move_computer)
            board_dict[i] = player
            break


def check_win(game_mode):
    if board_dict[1] == board_dict[2] == board_dict[3] == f'{current_player}' or \
            board_dict[4] == board_dict[5] == board_dict[6] == f'{current_player}' or \
            board_dict[7] == board_dict[8] == board_dict[9] == f'{current_player}' or \
            board_dict[1] == board_dict[5] == board_dict[9] == f'{current_player}' or \
            board_dict[3] == board_dict[5] == board_dict[7] == f'{current_player}' or \
            board_dict[1] == board_dict[4] == board_dict[7] == f'{current_player}' or \
            board_dict[2] == board_dict[5] == board_dict[8] == f'{current_player}' or \
            board_dict[3] == board_dict[6] == board_dict[9] == f'{current_player}':
        if game_mode == 1:
            if current_player == 'x':
                board()
                print(text_winner_player)
                exit()
            else:
                board()
                print(text_winner_computer)
                exit()
        elif game_mode == 2:
            if current_player == 'x':
                board()
                print(text_winner_x)
                exit()
            else:
                board()
                print(text_winner_o)
                exit()
    else:
        if not is_board_full():
            board()
            print(text_winner_both)
            exit()


def game(game_mode):
    while True:
        if game_mode == 1:
            while True:
                board()
                move('x')
                if check_win(game_mode) or is_board_full():
                    board()
                    computer_move('o')
                    if check_win(game_mode) or is_board_full():
                        continue
        elif game_mode == 2:
            while True:
                board()
                move('x')
                if check_win(game_mode) or is_board_full():
                    board()
                    move('o')
                    if check_win(game_mode) or is_board_full():
                        continue
