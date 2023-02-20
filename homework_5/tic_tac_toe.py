# Создайте программу для игры в "Крестики-нолики".
play_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
border_cell = 3


def print_board():
    print('_' * 4 * border_cell)
    for i in range(border_cell):
        print((' ' * border_cell + '|')*3)
        print(play_board[i*3], ' |', play_board[i*3+1],
              '|', play_board[i*3+2], '|')
        print(('_' * border_cell + '|')*3)


def game_step(index, char):
    if 1 > index > 9 or play_board[index-1] in ('X', 'O'):
        return False
    play_board[index-1] = char
    return True


def check_win():
    win = False
    win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for position in win_comb:
        if (play_board[position[0]] == play_board[position[1]] == play_board[position[2]]):
            win = play_board[position[0]]
    return win


def game_control():
    current_player = 'X'
    step = 1
    print_board()
    while (step < 10) and (check_win() == False):
        index = int(
            (input('Игрок ' + current_player + ' введите номер поля: ')))
        # доделать проверку если останется время
        if (game_step(index, current_player)):
            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'
            print_board()
            step += 1
        else:
            print('Клетка занята, поробуйте другую')
    if step == 10:
        print('Ничья. Игра окончена')
    else:
        print('Победитель ', check_win())


game_control()
