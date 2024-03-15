# # String - "Строки"
# # "Hello" 'Hello' 'без разницы в каких кавычках'
# # str1 = '''my 
# # name is Peter Parker. I'm SpiderMan \
# # '''
# # print(str1)

# # Строки - набор последовательных символов, которые мы используем для хранения и представления текстовой информации

# # Индексация в строке 
# # name = 'John'
# #         # J = 0 = -4
# #         # o = 1 = -3
# #         # h = 2 = -2 
# #         # n = 3 = -1
# # print(name[2])]

# # Срезы по индексам
# # [start: end: <step>] Важно
# # str1 = 'birthday'
# # print(str1)
# # print(str1[5:8])
# # print(str1[:5])
# # print(str1[5:])
# # text = "Hello World! My name is John Snow.I\'m King of North!"
# # print(text[:13:5])
# # print(text[::2])
# # print(text[::-1])


# # Конкатенация строк(соединение)
# # a = "Hello"
# # b = "World"
# # print(a + " " + b)
# # print(a,b+ " " + b , a)


# # Экранирование - способ записи символов,которые невозможно ввести с клавиатуры,либо же запись спец символов которые имеют функционал в питоне
# # \n -> перенос строки 
# # \t -> горизантальная табуляция
# # \v -> вертикальная табуляция
# # \' -> апостроф '\''

# # str1 = "\tHello world!\n\v\tHello John!\n'\\"
# # print(str1)

# # Форматирование строк
# # 1. с помощью %
# # 2. c использованием .format() метод
# # 3. интерполяция(преоброзование строк) f-stroki

# # name = input('Write your name: ')
# # last_name = input('Write your surname: ')
# # str1 = 'Hello mr 'and ' mrs %s %s ' %(name , last_name)
# # print(str1)

# # .format
# name = input('Write your name: ')
# last_name = input('Write your surname: ')
# # club = 'Kipish'
# # print('Welcome to the Club,{}, mr/mrs {} {} ' .format(club, name , last_name))

# # .f-stroki
# print(f"Hello brother {name} {last_name}")


# # legacy code - наследственный код

# Умножение строк(дублирование)
str1 = 'Kianu'
print(str1 * 3)
