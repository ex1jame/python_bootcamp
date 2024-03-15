# 1) Палиндром:

# Напишите программу, которая проверяет, является ли введенная пользователем строка палиндромом 
# (читается одинаково с начала и с конца, игнорируя пробелы, регистр букв).
# palindrom = "dad MOM                Dad   ".lower().split()
# print (palindrom == palindrom[::-1])
# print(palindrom)

# 2) Подсчет слов:

# Программа должна принимать текст и слово. Напишите программу,
#  которая подсчитывает количество слов в этом предложении.

# text = input( ).split()
# count_w = len(" ".join(text).split())
# print(count_w)
# 3) Генерация пароля:

# Напишите программу, которая генерирует случайный пароль заданной длины. 
# Пароль должен содержать как буквы, так и цифры.

# import random
# import string

# leng = 8
# characters = string.ascii_letters + string.digits + string.punctuation
# coun = 0
# password = ''
# while coun <= leng:
#     random_let = random.choice(characters)
#     password += random_let

#     coun += 1
# print(password)



 

# 4) Поиск повторяющихся символов:
# Напишите программу, которая проверяет, есть ли в веденной строке повторяющиеся символы.


# text = input(" ")
# duplicates = []
# for item in text:
#     if text.count(item) > 1 and item not in duplicates:
#         duplicates.append(item)


# print(duplicates)


# 5) Подсчет гласных и согласных:

# Введите строку, а затем напишите программу, которая подсчитывает количество гласных и согласных букв в ней.

text = " dsadsadsadsadas"
# 1) Палиндром:

# Напишите программу, которая проверяет, является ли введенная пользователем строка палиндромом 
# (читается одинаково с начала и с конца, игнорируя пробелы, регистр букв).
# palindrom = "dad MOM                Dad   ".lower().split()
# print (palindrom == palindrom[::-1])
# print(palindrom)

# 2) Подсчет слов:

# Программа должна принимать текст и слово. Напишите программу,
#  которая подсчитывает количество слов в этом предложении.

# text = input( ).split()
# count_w = len(" ".join(text).split())
# print(count_w)
# 3) Генерация пароля:

# Напишите программу, которая генерирует случайный пароль заданной длины. 
# Пароль должен содержать как буквы, так и цифры.

# import random
# import string

# leng = 8
# characters = string.ascii_letters + string.digits + string.punctuation
# coun = 0
# password = ''
# while coun <= leng:
#     random_let = random.choice(characters)
#     password += random_let

#     coun += 1
# print(password)



 

# 4) Поиск повторяющихся символов:
# Напишите программу, которая проверяет, есть ли в веденной строке повторяющиеся символы.


# text = input(" ")
# duplicates = []
# for item in text:
#     if text.count(item) > 1 and item not in duplicates:
#         duplicates.append(item)


# print(duplicates)


# 5) Подсчет гласных и согласных:

# Введите строку, а затем напишите программу, которая подсчитывает количество гласных и согласных букв в ней.

# text = input("Введите слово: ").upper()
# constant = "BCDFGHJKLMNPQRSTVWXZ"
# vowels = "AEIOUY"
# constant_count = 0
# vowels_count = 0
# symbol = 0
# for char in text: #Через for in
#     if char in constant:
#         constant_count += 1
#     if char in vowels:
#         vowels_count += 1
    
# while symbol < len(text): #Через while
    # if text[symbol] in constant: #Если text[символ = 0 индекс] проверяет в constant если ты там этот символ
        # constant_count += 1 # добавляет одно значение если условие подошло
#     else:   # если условие не подошло то гласная прибавляется
#         vowels_count += 1
#     symbol +=1 
#     print(constant_count,vowels_count)
    
     

