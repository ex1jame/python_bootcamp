"""
1) Напишите функцию -- чат-бот, который 
Всегда отвечает “Конечно!” на любой вопрос
Всегда отвечает “Успокойся”, если ты кричишь на него ВОТ ТАК!
Всегда отвечает “Как классно, когда ты молчишь. Продолжай в том же духе!” Если вызвал функцию, но ничего не передал.
В любых других случаях, отвечает “ну и что

”"""
# def func_chat_bot(n=None):
#     if n is None:
#         print("Как классно, когда ты молчишь. Продолжай в том же духе!")
#     elif n.endswith("ВОТ ТАК!"):
#         return "Успокойся"
#     elif n.endswith("?"):
#         return "Конечно!"
#     else:
#         return "ну и что"

# func_chat_bot()
# print(func_chat_bot('ВОТ ТАК!'))
# print(func_chat_bot('выьы'))

# print(func_chat_bot('FSDFSDF?'))



"""
2) Напишите функцию, которая принимает слово и возвращает True, если слово изограмма (т.е. все буквы в слове уникальны). Иначе возвращает False
"""
# def stingTrue(word : str):
#     word = word.lower()

#     unique_letter = set()

#     for letter in word:
#         if letter in unique_letter:
#             return False
#         else:
#             unique_letter.add(letter)
#     return True

# print(stingTrue('helo'))
"""
3) Подсчет букв:
Напишите функцию, которая принимает строку и возвращает словарь, 
в котором ключами являются буквы, а значениями — количество их вхождений в строку.
Регистр букв не должен учитываться.
"""
# def stringDict(string:str): 
#     string = string.lower()
#     dict_count = {}
#     for letter in string:
#         dict_count[letter] = dict_count.get(letter, 0) + 1
#     return dict_count
# print(stringDict('fsdfds'))


"""
4) Поиск подстроки:
Напишите функцию, которая принимает две строки и возвращает True, если вторая строка является подстрокой первой.
"""
# def substring(first,second):
#     return first in second
# print(substring('abc','abcdsd'))

"""
5) Напишите функцию, которая проверяет, сколько раз каждое слово в 
переданной фразе было использовано. Например: “Money, money, money, 
it’s always sunny, in the richmen’s world”. money: 3, it’s: 1, always: 1, 
sunny: 1, in: 1, the: 1, richmen’s: 1, world: 1.
"""
# def stringDict(string:str): 
#     string = string.lower()
#     string = string.split()
#     dict_count = {}
#     for word in string:

#         dict_count[word] = dict_count.get(word, 0) + 1
#     return dict_count
# print(stringDict('Money, money, money, it’s always sunny, in the richmen’s world'))
"""
6) Напишите функцию, которая принимает строку и выводит количество гласных, 
согласных букв и остальных символов. Используйте только кириллические символы
"""
# def russian_aplhabet(string:str):
#     vowel = 'аяуюоеёэиы'
#     constant = 'бвгджзйклмнпрстфхцчшщь'
#     count_vowel = 0
#     count_constant = 0
#     count_musor = 0
#     for i in string:
#         if i in vowel:
#             count_vowel += 1
#         elif i in constant:
#             count_constant += 1
#         else:
#             count_musor += 1
#     return f'Кол-во согласных {count_vowel}\nкол-во согласных {count_constant}\nкол-во мусора {count_musor}'
# print(russian_aplhabet('лталываькпшвамьвьмыджлвжыабэ-'))


"""
7) Вам дан список из нескольких имён в нижнем регистре. 
Напишите функцию которая записывает начинает первую букву имени в 
верхнем регистре и сохраните в новом списке.
"""
# lisfd = ['sereja','anton']

# def replaceUpper(name):
#     list_ = []
#     for up in name:
#         list_.append(up.capitalize())
        
#     return print(list_)

# replaceUpper(lisfd)




"""
8) Вам дан список из целых чисел. Напишите функцию, в которой Вам необходимо 
найти факториал каждого из чисел и записать в новый список.
"""
chisel = [1,2,3,4,5,6]
def factorial(listok:list):
    factorials = []
    for x in listok:
        res = 1
        for i in range(1,x + 1):
            res *= i
            factorials.append(res)
    return factorials
print(factorial(chisel))


"""
9) Вам дан список из чисел. Напишите функцию, которая вернёт новый список из квадратов этих чисел.
"""
# def calculate_squares(numbers):
#     squares = [x ** 2 for x in numbers]
#     return squares
# numbers = [1, 2, 3, 4, 5, 6]
# result = calculate_squares(numbers)
# print(result)
"""
10) Напишите функцию average, 
которая принимает список чисел и возвращает их среднее значение, НЕ используя встроенные функции sum и len
"""
def average(numbers):

    if not numbers:
        return None  

    total = 0
    count = 0

    for number in numbers:
        total += number
        count += 1

    return total / count
numbers = [1, 2, 3, 4, 5, 6]
result = average(numbers)
print(result)
