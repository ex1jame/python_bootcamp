# # # 1.Дано положительное число N. Вывести все числа от 0 до N с помощью цикла while.
# # # n = int(input("Введите положительное число "))
# # # print(n(range(0, n)))
# # s = range(0,10)
# # # count_n = 0
# # # while n > count_n:
# # #     symbol = range(0,n)
# # #     print(symbol) 
# # #     count_n += 1

# # print(s)

# # создайте алгоритм по нахождению ключа

# my_list = [
#     1,
#     'string',
#     [1, 2, 3, 4, 5, 6, 7, 8, 'python', ['hub', 'history', 'key']],
#     'hello',
#     False,
#     None,
#     'key',
#     [0, 1, 2, 3, 4],
#     3.14,
#     ['apple', 'banana', 'cherry'],
#     [9, 8, 7, [6, 5, [4, 3, [2, 1]],'key']],
#     True,
#     'world',
#     [10, [20, [30, [40, [50, [60, [70, [80, [90]]]]],['welcome', 1,2,3,4, 'programm'],'key']]],'key']
# ]
# keys = 'key'
# for x in my_list:
#     if x == keys:
#         print(x)
# import random 
# # ls = []
# # x = 0
# # while x<10:
# #     heh=random.randint(0,11)
# #     ls.append(heh)
# #     x +=1
# # print(ls)

# # x = 11
# # counter = 0
# # if counter < 10:
# #     ls.append(list(range(1,11)))
# #     counter += 1
# # print(ls)
# # element = list(range(1,11))
# # for x in element:
# #     ls.append(x)
# # print(ls)
# # print(element)\



# dict_ = {
#     'A': '.-', 
#     'B': '-...', 
#     'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
#     'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
#     'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#     'Y': '-.--', 'Z': '--..',
#     '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#     '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
# }
# # adsdm = {}
# # user = 'hallo'.upper() #input('enter smth: ')
# # for i in list(user):
# #     for k,v in dict_.items():
# #         if i == k:
# #             adsdm[k] = v
# #         # if i == dict_.items():
# #         # print(dict_.values(i))
# #         # print("sadfsafdsnf")
# # print(adsdm)from random import shuffle, sample

# from random import shuffle, sample

# list_range = list(range(1, 76))  # Corrected to exclude 0
# list_bingo = ['B', 'I', 'N', 'G', 'O']
# result_list = [i + str(x) for i in list_bingo for x in list_range]
# shuffle(result_list)

# simulations = 1000
# draws_list = []

# for _ in range(simulations):
#     if len(result_list) < 5:
#         # If there are fewer than 5 elements in result_list, break out of the loop
#         break

#     winning_lot = set(sample(result_list, k=5))
#     matrix = [[x + str(_) for _ in sample(list_range, k=5)] for x in list_bingo]

#     draws = 0
#     selected_numbers = set()

#     while not all(set(row) <= selected_numbers for row in matrix):
#         draws += 1
#         if result_list:
#             number = result_list.pop()
#             selected_numbers.add(number)

#     draws_list.append(draws)

# # Check if draws_list is empty before calculating statistics
# if draws_list:
#     # Display the results
#     print("Минимальное количество извлечений:", min(draws_list))
#     print("Максимальное количество извлечений:", max(draws_list))
#     print("Среднее количество извлечений:", sum(draws_list) / len(draws_list))
# else:
#     print("Невозможно провести достаточное количество симуляций.")

from tkinter import *
from tkinter import ttk

tasks = Tk()
tasks.title("Calculator")
display_text = Entry(tasks,
                     font=('arial', 20,'bold'),
                     textvariable="",
                     bd=30,
                     insertwidth=4,
                     bg="powder blue",
                     justify=RIGHT)
display_text.grid()

tasks.mainloop()