# Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) (доп) Подумайте как наделить бота ""интеллектом""


# import Funct_for_dz5 as PF
# import random
#
#
# def game_players(num_of_players=2, candy_ammount=2021, aloud_ammount_on_turn=28):
#     """Игра - где каждый игрок по очереди берёт доступное кол-во конфет
#     Args:
#         num_of_players (int, optional): Кол-во игроков Defaults to 2.
#         candy_ammount (int, optional): Всего конфет. Defaults to 2021.
#         aloud_ammount_on_turn (int, optional):Можно брать за раз. Defaults to 28.
#     """
#     list_of_players = [i for i in range(1, num_of_players + 1)]
#     i = 0
#     while candy_ammount > 0:
#         if aloud_ammount_on_turn > candy_ammount:
#             aloud_ammount_on_turn = candy_ammount
#         candy_take = PF.input_number_examination(
#             text_in_input=f"Candy left : {candy_ammount} \tPlayer {list_of_players[i]} :", case_def=3, min_num=1,
#             max_num=aloud_ammount_on_turn)
#         candy_ammount -= candy_take
#         if candy_ammount == 0:
#             break
#         else:
#             if i == num_of_players - 1:
#                 i = 0
#             else:
#                 i += 1
#
#     print(f"Player {list_of_players[i]} took last candy ! he WON! ")
#
#
# def game_bot_easy(candy_ammount=2021, aloud_ammount_on_turn=28):
#     """Игра против бота, бот рандомно берёт кол-во конфет
#     Args:
#         candy_ammount (int, optional): Всего конфет. Defaults to 2021.
#         aloud_ammount_on_turn (int, optional): Кол-во конфет за ход. Defaults to 28.
#     """
#     start = input("Press enter to start")
#     tos_a_coin = random.randint(0, 2)
#     if tos_a_coin == 0:
#         list_of_players = ["Player", "Bot"]
#         print("Player go first \n")
#     else:
#         list_of_players = ["Bot", "Player"]
#         print("Bot go first \n")
#     i = 0
#     while candy_ammount > 0:
#         if aloud_ammount_on_turn > candy_ammount:
#             aloud_ammount_on_turn = candy_ammount
#         if list_of_players[i] == "Player":
#             candy_take = PF.input_number_examination(
#                 text_in_input=f"Candy left : {candy_ammount} \t{list_of_players[i]} :", case_def=3, min_num=1,
#                 max_num=aloud_ammount_on_turn)
#         else:
#             candy_take = random.randint(1, aloud_ammount_on_turn)
#             print(f"Candy left : {candy_ammount} \t{list_of_players[i]} : {candy_take}")
#         candy_ammount -= candy_take
#         if candy_ammount == 0:
#             break
#         else:
#             if i == 1:
#                 i = 0
#             else:
#                 i = 0
#
#     print(f"Player {list_of_players[i]} took last candy ! he WON! ")
#
#
# def game_2_bots_easy(candy_ammount=2021, aloud_ammount_on_turn=28):
#     """Игра 2 ботов , каждый из которых берёт рандомное кол-во конфет
#     Args:
#         candy_ammount (int, optional): Кол-во всего конфет. Defaults to 2021.
#         aloud_ammount_on_turn (int, optional): Кол-во конфет за раз. Defaults to 28.
#     """
#     start = input("Press enter to start")
#     tos_a_coin = random.randint(0, 2)
#     if tos_a_coin == 0:
#         list_of_players = ["Player", "Bot"]
#         print("Player go first \n")
#     else:
#         list_of_players = ["Bot", "Player"]
#         print("Bot go first \n")
#     i = 0
#     while candy_ammount > 0:
#         if aloud_ammount_on_turn > candy_ammount:
#             aloud_ammount_on_turn = candy_ammount
#
#         if candy_ammount <= aloud_ammount_on_turn * 2 and candy_ammount > 29:
#             candy_take = candy_ammount - 29
#         elif candy_ammount <= aloud_ammount_on_turn:
#             candy_take = candy_ammount
#         else:
#             candy_take = random.randint(1, aloud_ammount_on_turn)
#
#         print(f"Candy left : {candy_ammount} \t{list_of_players[i]} : {candy_take}")
#         candy_ammount -= candy_take
#         if candy_ammount == 0:
#             break
#         else:
#             if i == num_of_players - 1:
#                 i = 0
#             else:
#                 i += 1
#
#     print(f"Player {list_of_players[i]} took last candy ! he WON! ")
#
#
# def game_bot_2_medium(candy_ammount=2021, aloud_ammount_on_turn=28):
#     """В этом варианте - бот по концеове старается выйграть , точнее если игрок не будет просчитывать ходы - бот точно выйграет
#     Args:
#         candy_ammount (int, optional): Кол-во конфет всего. Defaults to 2021.
#         aloud_ammount_on_turn (int, optional): Кол-во конфет за ход. Defaults to 28.
#     """
#     start = input("Press enter to start")
#     tos_a_coin = random.randint(0, 2)
#     if tos_a_coin == 0:
#         list_of_players = ["Player", "Bot"]
#         print("Player go first \n")
#     else:
#         list_of_players = ["Bot", "Player"]
#         print("Bot go first \n")
#     i = 0
#     while candy_ammount > 0:
#         if aloud_ammount_on_turn > candy_ammount:
#             aloud_ammount_on_turn = candy_ammount
#         if list_of_players[i] == "Player":
#             candy_take = PF.input_number_examination(
#                 text_in_input=f"Candy left : {candy_ammount} \t{list_of_players[i]} :", case_def=3, min_num=1,
#                 max_num=aloud_ammount_on_turn)
#         else:
#             if candy_ammount >= aloud_ammount_on_turn * 2 + 1 and candy_ammount < aloud_ammount_on_turn * 3:
#                 candy_take = candy_ammount - (aloud_ammount_on_turn * 2)
#             elif candy_ammount <= aloud_ammount_on_turn * 2 and candy_ammount > 29:
#                 candy_take = candy_ammount - 29
#             elif candy_ammount <= aloud_ammount_on_turn:
#                 candy_take = candy_ammount
#             else:
#                 if candy_ammount <= aloud_ammount_on_turn * 2 and candy_ammount > 29:
#                     candy_take = candy_ammount - 29
#                 elif candy_ammount <= aloud_ammount_on_turn:
#                     candy_take = candy_ammount
#                 else:
#                     candy_take = random.randint(1, aloud_ammount_on_turn)
#             print(f"Candy left : {candy_ammount} \t{list_of_players[i]} : {candy_take}")
#         candy_ammount -= candy_take
#         if candy_ammount == 0:
#             break
#         else:
#             if i == num_of_players - 1:
#                 i = 0
#             else:
#                 i += 1
#
#     print(f"Player {list_of_players[i]} took last candy ! he WON! ")
#
#
# candy_ammount = 2021
# aloud_ammount_on_turn = 28
#
# print(f"Игра - забери последнюю конфету !\nправила: есть {candy_ammount}\nза раз можно взять {candy_ammount}\nцель, забрать последнюю конфету !\n")
# print("есть выбор :\n1 - игра с компанией, от 2 до 6 человек\n2 - посмотреть как играют 2 бота\n4 - игра против слабого бота\n3 - игра против среднего бота\n")
# coise_case = PF.input_number_examination(text_in_input="Выш выбор : ", case_def=3, min_num=1, max_num=4)
# match coise_case:
#     case 1:
#         num_of_players = PF.input_number_examination(text_in_input="Кол-во игроков от 2х до 6и : ", case_def=3, min_num=2, max_num=6)
#         game_players(num_of_players, candy_ammount, aloud_ammount_on_turn)
#     case 2:
#         game_bot_easy(candy_ammount, aloud_ammount_on_turn)
#     case 3:
#         game_2_bots_easy(candy_ammount, aloud_ammount_on_turn)
#     case 4:
#         game_bot_2_medium(candy_ammount, aloud_ammount_on_turn)


# Создайте программу для игры в ""Крестики-нолики"".


# import Funct_for_dz5 as PF
# import os
#
# def print_game_board(game_list : list):
#     """Печатает доску для игры
#     Args:
#         game_list (list): Принимает на вход доску для игры
#     """
#     os.system('cls')
#     for i in game_list:
#         result = ""
#         for j in i:
#             result += f"\t{j}"
#         print(result)
#         print("\n")
#
# game_list = []
# pos_dic ={}
#
# # Cоздаётся массив, в который записываются номера от 1 до 9. Что бы не играться с координатами
# # потом словарь с этими координатами.
#
# index = 1
# for i in range(0,3):
#     list_new = []
#     for j in range(0,3):
#         list_new.append(index)
#         index +=1
#     game_list.append(list_new)
#
# print_game_board(game_list)
#
# for i in range(0,3):
#     for j in range(0,3):
#         pos_dic[game_list[i][j]] = [i,j]
#
# def win_chek(pos_dic : dict,game_list : list) -> bool:
#     win_bool = False
#     if game_list[pos_dic[1][0]][pos_dic[1][1]] == game_list[pos_dic[2][0]][pos_dic[2][1]] == game_list[pos_dic[3][0]][pos_dic[3][1]]:
#         win_bool = True
#     elif game_list[pos_dic[4][0]][pos_dic[4][1]] == game_list[pos_dic[5][0]][pos_dic[5][1]] == game_list[pos_dic[6][0]][pos_dic[6][1]]:
#         win_bool = True
#     elif game_list[pos_dic[7][0]][pos_dic[7][1]] == game_list[pos_dic[8][0]][pos_dic[8][1]] == game_list[pos_dic[9][0]][pos_dic[9][1]]:
#         win_bool = True
#     elif game_list[pos_dic[1][0]][pos_dic[1][1]] == game_list[pos_dic[4][0]][pos_dic[4][1]] == game_list[pos_dic[7][0]][pos_dic[7][1]]:
#         win_bool = True
#     elif game_list[pos_dic[2][0]][pos_dic[2][1]] == game_list[pos_dic[5][0]][pos_dic[5][1]] == game_list[pos_dic[8][0]][pos_dic[8][1]]:
#         win_bool = True
#     elif game_list[pos_dic[3][0]][pos_dic[3][1]] == game_list[pos_dic[6][0]][pos_dic[6][1]] == game_list[pos_dic[9][0]][pos_dic[9][1]]:
#         win_bool = True
#     elif game_list[pos_dic[1][0]][pos_dic[1][1]] == game_list[pos_dic[5][0]][pos_dic[5][1]] == game_list[pos_dic[9][0]][pos_dic[9][1]]:
#         win_bool = True
#     elif game_list[pos_dic[3][0]][pos_dic[3][1]] == game_list[pos_dic[5][0]][pos_dic[5][1]] == game_list[pos_dic[7][0]][pos_dic[7][1]]:
#         win_bool = True
#     return win_bool
#
#
# player_turn = 2
# turns_count = 0
#
#
# while not win_chek(pos_dic,game_list) and turns_count != 9:
#
#     if player_turn == 1:
#         player_turn = 2
#     else:
#         player_turn = 1
#     position_bool = True
#     print("Введите номер ячеки куда поставить символ от 1 до 9 : ")
#     while position_bool:
#         possition_to_put = PF.input_number_examination(text_in_input=f"Игрок {player_turn} ",case_def=3,min_num=1,max_num=9) # ввод числа от 1 до 9
#         if game_list[pos_dic[possition_to_put][0]][pos_dic[possition_to_put][1]] == possition_to_put : # проверка - если эта ячейка уже занята
#             if player_turn == 1:
#                 game_list[pos_dic[possition_to_put][0]][pos_dic[possition_to_put][1]] = "X" # Х если игрок 1
#                 position_bool = False
#             else :
#                 game_list[pos_dic[possition_to_put][0]][pos_dic[possition_to_put][1]] = "O" # О если игрок 2
#                 position_bool = False
#         else:
#             print("Ячейка занята, попробуйте другую")
#
#     turns_count += 1
#
#     print_game_board(game_list)
#
# if turns_count == 9 and not win_chek(pos_dic,game_list):
#     print(f"Победила дружба !")
# else:
#     print(f"Игрок {player_turn} выйграл")




# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res
#
# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res
#
#
# s = input("Введите текст для кодировки: ")
# print(f"Текст после кодировки: {coding(s)}")
# print(f"Текст после дешифровки: {decoding(coding(s))}")