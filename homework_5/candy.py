# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random


def players_data():
    player = {
        'player_turn': False
    }
    player['name'] = input('Введите ваше имя: ')
    return player


print('Игрок 1')
player_1 = players_data()
print('Игрок 2')
player_2 = players_data()


def first_player():
    first_player = random.randint(1, 2)
    if first_player == 1:
        player_1['player_turn'] = True
    else:
        player_2['player_turn'] = True


first_player()

candys = 2021

while candys > 0:
    if candys == 1 and player_1['player_turn'] == True:
        print(f"Победил игрок {player_2['name']}")
        break
    elif candys == 1 and player_2['player_turn'] == True:
        print(f"Победил игрок {player_1['name']}")
    else:
        if player_1['player_turn'] == True:
            while True:
                player_1_score = int(
                    input(f"{player_1['name']}, сколько конфет берете? "))
                if 0 < player_1_score <= 28:
                    candys = candys - player_1_score
                    print(candys)
                    player_1['player_turn'] = False
                    player_2['player_turn'] = True
                    break
                else:
                    print(
                        f"{player_1['name']}, за один ход вы можете взять не более 28 конфет")
        else:
            while True:
                player_2_score = int(
                    input(f"{player_2['name']}, сколько конфет берете? "))
                if 0 < player_2_score <= 28:
                    candys = candys - player_2_score
                    print(candys)
                    player_1['player_turn'] = True
                    player_2['player_turn'] = False
                    break
                else:
                    print(
                        f"{player_1['name']}, за один ход вы можете взять не более 28 конфет")
