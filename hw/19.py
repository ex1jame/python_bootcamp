

# 1 задача:

   

#  Напишите программу, которая симулирует игру лото с одной картой.
#  Начните с генерирования списка их всех возможных номеров выпадения (от В1 до О75).
#  После этого перемешайте номера в хаотичном порядке, воспользовавщись функцией shuffle 
# из модуля random. Вытаскивайте по одному номеру из списка и зачеркивайте номера, пока 
# карточка не окажется выигравшей. Приведите 1000 симуляций и выведите на экран минимальное
# , максимальное и среднее количество извлечений номеров, требующееся для выигрыша.
from random import shuffle,sample
list_range = range(0,76)
list_bingo = ['B','I','N','G','O']
# Создаем 100 разных билетов
# num_matrices = 1000
# matrices = []
# for _ in range(num_matrices):
#     matrix = [[x + str(_) for _ in sample(list_range, k=5)] for x in list_bingo]
#     matrices.append(matrix)
# for bilet in matrices:
#     print('--------------------------------------')
#     for row_1 in bilet:
#         print(row_1)
# ---------------------------------------------------------------
res = []
for _ in range(10):
    # количество извлечений номеров
    draw = 0
    bilet = [[x + str(_) for _ in sample(list_range, k=5)] for x in list_bingo]
    
    # мешок из которого достаем рандомный номер билета

    result_list = []
    for i in list_bingo:
        for x in list_range:
            result_list.append(i +str(x))
    shuffle(result_list)
    # Создаем два списка с диагоналями
    diagonals = [[], []]
    i = 0
    i2 = -1
    for row in bilet:
        diagonals[0].append(row[i])
        diagonals[1].append(row[i2])
        i += 1
        i2 -= 1

    flag = True
    while flag:
        number = result_list.pop()
        draw += 1

        # Проверка выигрыша по горизонтали
        for row in bilet:
            if number in row:
                row[row.index(number)] = 'X'
                if all(cell == 'X' for cell in row):
                    flag = False

        # Проверка по вертикали
        for i in range(5):
            column = [row[i] for row in bilet]
            if all(cell == 'X' for cell in column):
                flag = False

        # Проверка по диагонали
        for diagonal in diagonals:
            if number in diagonal:
                diagonal[diagonal.index(number)] = 'X'
                if all(cell == 'X' for cell in diagonal):
                    flag = False
    res.append(draw)
    draw = 0
print(res)
print(f'Максимальное количество вытаскиваний номеров из мешка равно {max(res)}\nМинимальное количество вытаскиваний номеров из мешка равно {min(res)}')
# matrix = [[x + str(_)for _ in sample(list_range, k=5)] for x in list_bingo]
# lists = [matrix for _ in range(101)]
# for row in lists:
#     print(row)
# # winner = []
# for row in matrix:
#     print(row)
# for win_lot in winning_lot:
#     for col in matrix[0]:
#         for lot in col:
#             if win_lot in lot:
#                 winner.append(win_lot)
#                 print(winner)
#     for col in matrix[1]:
#         for lot in col:
#             if win_lot in lot:
#                 winner.append(win_lot)
#                 print(winner)
#     for col in matrix[2]:
        
#         for lot in col:
#             if win_lot == lot:
#                 winner.append(lot)
#                 print(winner)

#     for col in matrix[3]:
#         for lot in col:
#             if win_lot == lot:
#                 winner.append(lot)
#                 print(winner)

#     for col in matrix[4]:
#         for lot in col:
#             if win_lot == lot:
#                 winner.append(lot)
#                 print(winner)

# print(winner)
            
            

# # 1 действие достаем из листа бинго первую букву
# # 2 действие достаем уникальный цифру через семпл а в кей указан количество доставаний
# # 3 конкатенируем букву на число заранее обернутую в строку 
#     # draws = 0
#     # selected_numbers = set()
#     # while not all(set(row) <= selected_numbers for row in matrix):
#     #     draws += 1
#     #     if result_list:
#     #         number = result_list.pop()
# #             selected_numbers.add(number)

# #     draws_list.append(draws)
# # if draws_list:
# #     print("Минимальное количество извлечений:", min(draws_list))
# #     print("Максимальное количество извлечений:", max(draws_list))
# #     print("Среднее количество извлечений:", sum(draws_list) / simulations)
# # else:
# #     print("vse govno ")
# # for row in matrix:
# #     print(row)

# # winning_lot = []
# # for i in result_list:
# #     winning_lot.append(i)
# #     break
# # # print(winning_lot)

# # ls = [matrix[0][0],matrix[1][1],matrix[2][2],matrix[3][3],matrix[4][4]]
# # ls2 = [matrix[0][-1],matrix[1][-2],matrix[2][-3],matrix[3][-4],matrix[4][-5]]
# # winning_numbers = set()
# # draws = 0

# # while not all(set(row[1:]) <= winning_numbers for row in matrix):
# #     draws += 1
# #     number = result_list.pop()
# #     winning_numbers.add(number)

# # ls3 = []
# # for i in matrix:
# #     for x in row:
# #         print(x)
#         # ls3.append(x)
#         # print(ls3)
#         # break

# # print(ls)
# # # print(ls2)
# # import random

# # atempant = []
# for _ in range(1000):
#     all_numbers = [f'{letter}{number}' for letter in 'BINGO' for number in range(1, 76)]
#     random.shuffle(all_numbers)

    
#     card_generate = [['B67', 'B18', 'B28', 'B27', 'B8'], 
#                      ['I60', 'I69', 'I29', 'I17', 'I35'],
#                        ['N16', 'N68', 'N17', 'N1', 'N57'],
#                          ['G26', 'G48', 'G56', 'G71', 'G22'],
#                     ['O33', 'O44', 'O69', 'O13', 'O9']]


#     check = True
#     counter = 0
#     while check:

#         counter += 1

        
#         delete_num = random.choice(all_numbers)
#         all_numbers.remove(delete_num)

#         for row in card_generate:
#             if delete_num in row:  
#                 row[row.index(delete_num)] = 'X'
    
#         for row in card_generate:
#             if len(set(row)) == 1:
#                 atempant.append(counter)
#                 # for _ in card_generate:
#                 #     print(_)
#                 check = False
#                 break

#         for col in range(0, 5):
#             if len(set(row[col] for row in card_generate)) == 1:
#                 # for _ in card_generate:
#                 #     print(_)
#                 atempant.append(counter)
#                 check = False
#                 break


                                    
#         if len(set(card_generate[i][i] for i in range(5))) == 1 or len(set(card_generate[i][4-i] for i in range(5))) == 1:
#             # for _ in card_generate:
#             #     print(_)
#             atempant.append(counter)
#             check = False
#             break
#             # break
#     # print()
#     # for i in card_generate:
#     #     print(i)

# print(len(atempant))

# print(f'Min: {min(atempant)}')
# print(f'Max: {max(atempant)}')
# print(f'Average: {atempant[sum(atempant) // len(atempant)]}')



# # 2 задача:

# #     Азбука Морзе зашифровывает буквы и цифры при помощи точек и тире.
# #     В данном упражнении вам необходимо написать программу, в которой
# #     соответствие символов из азбуки Морзе будет храниться в виде словаря.
# #     В табл. 6.3 приведена та часть азбуки, которая вам понадобится при ре-
# #     шении этого задания.
# #     В основной программе вам необходимо запросить у пользователя стро-
# #     ку. После этого программа должна преобразовать его в соответствующую
# #     последовательность точек и тире, вставляя пробелы между отдельными120  Упражнения
# #     символами. Символы, не представленные в таблице, можно игнорировать.
# #     Например, сообщение Hello, World! может быть представлено следующей
# #     последовательностью: .... . .–.. .–.. ––– .–– ––– .–. .–.. –..
# #     Таблица 6.3. Азбука Морзе

# #     Символ     Код     Символ     Код     Символ     Код     Символ     Код
# #     A               .–        J                 .–––     S               ...        1               .––––
# #     B               –...      K                –.–       T               –           2              ..–––
# #     C               –.–.      L                .–..      U               ..–        3              ...––
# #     D               –..       M               ––         V              ...–        4              ….–
# #     E               .          N                –.         W             .––         5             …..
# #     F               ..–.      O                –––       X              –..–        6             –….
# #     G               ––.       P                .––.      Y              –.––        7             ––...
# #     H               ….       R                ––.–     Z              ––..         8            –––..
# #     I                ..         S                .–.        0              –––––      9            ––––.
# # dict_ = {
# #     'A': '.-', 
# #     'B': '-...', 
# #     'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
# #     'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
# #     'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
# #     'Y': '-.--', 'Z': '--..',
# #     '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
# #     '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
# # }
# # adsdm = {}
# # user = 'hallo'.upper() #input('enter smth: ')
# # for i in list(user):
# #     for k,v in dict_.items():
# #         if i == k:
# #             adsdm[k] = v
# #         # if i == dict_.items():
# #         # print(dict_.values(i))
# #         # print("sadfsafdsnf")
# # print(adsdm)
# # user = input('Enter a sentence: ').upper()
# # ls = []
# # for i in list(user):
# #     print(i)
# #     if i == ',' or i == '?':
# #         continue
# #     for k,v in dict_.items():
# #         if i == k:
# #             ls.append(v)
# # print(' '.join(ls)) 