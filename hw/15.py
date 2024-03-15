"""=================EASY=================="""
# /// TASK1 \\\
# Дан список целых чисел, найдите минимальное значение, не используя встренную функцию min()
# Например:
# list_ = [20, 10, 20, 1, 100]
# # Результат:
# # min_number = 1
# min_num = list_[3]
# for i in list_:
#     if i <= min_num:
#         print(f"min_number = {min_num}")




# /// TASK2 \\\
# Дан список с кортежами, выведите список без пустых кортежей
# Например:
# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# # Результат:
# # cleared_tuples = [('ram','15','8'), ('laxman', 'sita')]
# for x in tuples:
#     if x == ():
#         tuples.remove(x)
# print(tuples)




# /// TASK3 \\\
# Запросите у пользователей 5 раз их имя и фамилию, но в списке сохраните лишь фамилию, также учтите, что
# у человека ФИО может состоять не только из 2 слов. При выводе должен выходить отсортированный
# в алфавитном порядке список
# surname_ls = []
# i = 5

# while i > 0:
#     if i > 0:
#         name_surname = input('Введите имя и фамилию через пробел: ').split()
#         surname = name_surname[1]
#         i -= 1
#         surname_ls.append(surname)
# surname_ls.sort()
# print(surname_ls)
    
    
    


    
# Наример:
# Name: Maya Angelou
# Name: Chimamanda Ngozi Adichie
# Name: Tobias Wolff
# Name: Sherman Alexie
# Name: Jane Austen
# Результат:
# ['Adichie', 'Alexie', 'Angelou', 'Austen', 'Wolff']





# /// TASK4 \\\
# Вам дан список из чисел, и переменная x в которой хранится число, 
# посчитайте сколько вхождений этого числа в этом списке 

# Например:
# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# x = 8
# # Результат:
# # 5
# count = 0
# for i in list_:
#     if i == x:
#         count += 1
# print(count)




# /// TASK5 \\\
# Вам дан список с числами и строками, найдите сумму чисел в
#  этом списке не используя функцию sum()
# Например:
# lists = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# # Результат:
# # 20
# # sum([1,3,1.2,4,5,7,-5,-12.22]) 
# sum1 = 0
# for i in lists:
#     if isinstance(i,(float,int)):
#         sum1 += i
# print(sum1)




# /// TASK6 \\\
# Вам дан список из строк, в которых длина строки равна 2 или более, 
# в новый список запишите индексы тех строк, у которых
# первый и последний символы совпадают.
# Например:
# str_list = ['abc', 'xyz', 'aba', '1221']
# index_list = []
# for i,x in enumerate(str_list):
#     if x[0] == x[-1]:
#         index_list.append(i)
# print(f"index = {index_list}")
            

# Результат:
# indexs = [2, 3]








# /// TASK7 \\\
# У вас есть список со вложенными списками, 
# выведите самый длинный список и самый короткий
# Например:
# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_list = max(lists, key=len)
# min_list = min(lists, key=len)
# print("max_list", max_list)
# print("min_list", min_list)

# Результат:
# max_list [13, 15, 17]
# max_list [0]





# /// TASK8 \\\
# Вам дан список, напишите код, который будет соединять в новый список элементы 
# по n-ному шагу
# Например:
# n = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# # Результат:
# # [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
# result = []
# for i in range(n):
#     append_time=list_[i::n]
#     result.append(append_time)
# print(result)
    

# /// TASK9 \\\
# Напишите код для создания матрицы с размером 3x3
# Результат:
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# matrix =[]
# for i in range(3):
#     row = [1,2,3]
#     matrix.append(row)
# print(matrix)



# /// TASK10 \\\
# Вам дан список со словами, пользователь вводит первую букву слова, которое он ищет, 
# ваш код должен вывести список со всеми словами начинающимися на эту букву
# Например:
# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
# # хочу найти слово начинающееся на букву 's'
# # Результат:
# # ['sun', 'stranger']
# result = []
# for i in list_:
#     if i[0] == 's':
#         result.append(i)
# print(result)
        





"""=====================MEDIUM========================"""

# /// TASK1 \\\
# Вам даны 2 списка, напишите код, который будет выводить разницу 
# первого списка от второго и наоборот
# # Например:
# color1 = ["red", "orange", "green", "blue", "white"]
# color2 = ["black", "yellow", "green", "blue"]
# # Результат:
# # Color1-Color2:  ['red', 'white', 'orange']
# # Color2-Color1:  ['black', 'yellow']
# color3 = set(color1)-set(color2)
# color4 = set(color2)-set(color1)

# print(color3)
# print(color4)




# /// TASK2 \\\
# Вам даны 2 списка из чисел, нужно написать код, который будет выводить True, если есть хотя бы один общий элемент,
# в ином случае False
# Например:
# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]
# # Результат:
# # True
# found_ = False

# for i in list1:
#     for x in list2:
#         if i == x:
#             found_=True
# print(found_)



# /// TASK3 \\\
# Ван дан список, выведите числа, частота повторений которых больше или равно K
# Например:
# list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
# res = []
# # Результат:
# # res = [4, 3, 8]
# for i in list_:
#     if i == 4:
#         res.append(i)
#     if i == 3:
#         res.append(i)
#     if i == 8:
#         res.append(i)
# print(set(res))
        








# /// TASK4 \\\
# Вам дан список из 3 чисел, выведите все возможные комбинации с этими числами
# Например:
# import itertools
# list_ = [1, 2, 3]
# permutations = list(itertools.permutations(list_))
# for i in permutations:
#     print(i)
# for i in itertools.product(list_, repeat = 3):
#     print(i)
# Результат:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1






# /// TASK5 \\\
# Создайте список с 3 вложенными списками списками, где внутри должно быть три 0
# Результат:
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# list_ = []

# for i in range(3):
#     row = [0,0,0]
#     list_.append(row)
# print(list_)






# /// TASK6 \\\
# Вам дан список со строками, необходимо перевернуть эти строки, а также отсортировать по длине
# Например:
# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# # # Результат:
# # # ['deR', 'eulB', 'neerG', 'etihW', 'kcalB', 'wolleY', 'egnarO']
# sorteds = sorted((color[::-1] for color in colors),key = len)
# print(sorteds)


# /// TASK 7 \\\
# Вам дан список с элементами, добавьте элемент, который хранится 
# в переменной x в этот список после каждого n-ого шага
# Например:
# nums = [1,2,3,4,5,6,7,8,9,0]
# n = 2
# x = 'a'
# # Результат:
# # [1, 2, 'a', 4, 'a', 6, 'a', 8, 'a', 0]
# for i in range(n,len(nums) + n, n):
#     nums.insert(i,x)

# print(nums)





"""=================HARD===================="""
# /// TASK1 \\\
# Вам дан список со вложенными списками, выведите тот список, у которого самая большая сумма
# Например:
# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# # Результат:
# # [10, 11, 12]




# max_chay = max(lists , key = sum)
# print(max_chay)


# /// TASK2 \\\
# Дан список целых чисел с повторяющимися элементами. Вам надо создать еще один список, содержащий только 
# повторяющиеся элементы. Проще говоря, новый список должен содержать элементы, которых больше одного.
# Например:
list_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Результат:
# repeated = [20, 30, -20, 60]
# repeted_list = []
# unique_set = set()
# duplicates = (x for x in list_ if x in unique_set or unique_set.add(x))
# print(set(duplicates))








# /// TASK3 \\\
# Вам дан список из букв, пользователь вводит 2 буквы, от какой и до 
# какой буквы нужно соединить в одну строку, 
# ваш код должен соединить эти буквы
# Например:
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
froms = 'a'
to = 'd'    
# Результат:
# ['abcd', 'e', 'f', 'g']
if froms in chars and to in chars:
    start_froms = chars.index(froms)
    end_to = chars.index(to)

result_string = ''.join(chars[start_froms:end_to + 1])
chars[start_froms:end_to + 1] = [result_string]
print(chars)
