text = 'The more you learn, the more you earn.'
# len() - возвращает длину строкиб считая каждый ее символ
len_text = len(text)
# print(len_text) 
# print(text[5:6:])
# print(text[::-1])

count_e = 0
i = 0
while i < len_text:
    symbol = text[i]
    if symbol == 'e' or symbol =='E':
        count_e += 1
    print(symbol)
    i += 1

print(f'Symbol E is found: {count_e} times!1')

# custom len code
# text = 'The more you learn, the more you earn.'

# i = 0

# while text[i:]:
#     i += 1
   
# print(i)


# ------------------------------------------------

# Методы строк - dir()
# print(dir("123"))

# Методы строк
text1 = 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 
'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit','rstrip', 
'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'   

# count(value, [start]) - считает кол-во вхождений value в нашу строку
# text = "hello o o o o hello"
# print(text1.count( ))

# replace(old, new, [count]) - меняет в строке old символ на new, заменит count  раз если передаете число
# text = ' ha h hah hah hah ah ah ah ah ah a ha ha ah ahaaha h ah ah its time Joker'
# res = text.replace('a','e', 4)
# print(f'original text: {text}')
# print(f'NOT original text: {res}')

# strip() - Убирает пробельные символы в начале и в конце строки
# rstrip, lstrip
# a = '   Hello   '
# print(a ,len(a), sep='->')
# res = a.strip()
# print(res, len(res), sep='->')
# print(a.lstrip(), '1')

# isdigit -         ПРОВЕРЯЕТ
# isnumeric - состоит ли наша строка
# isdecimal -   полностью из чисел

# num = input('Write number: ')
# print(f'Wrote li number?: {num.isdigit()}')

# isalpha - состоит ли наша строка из символов алфавита
# print(('Hello world'.replace(' ','')).isalpha())

# num = input('Vvedite chislo: ')
# if num.isdigit():
#     num = int(num)
#     print(f'{num} * 5 = {num * 5}')
# else:
#     print('Vy vveli ne chislo')

# split(separator) - дробит(разделяет) строку на несколько частей по разделителю,
# все части сохраняются в типе list
# разделяет по пробелу
# может разделять по символам и также если ничего не дать сплиту разделится по словам

# text = 'Let me speak in English!'
# print(text.split( ))

# a = '#hello#life#work#love#bishkek'
# print(a)
# print(a[1:].split('#')) #добавили [1:] что бы начал разделять с первого индекса [start: end:]


# 'connector'.join(list) - соединяет по connector строки которые были в list

# ls = ['Anvar', 'Jonh', 'Anarbek', 'Temirlan','Diana','Bolot']
# print(ls)
# res1 = ''.join(ls)
# res = '-'.join(ls)
# print(res1)
# print(res)

# swapcase( ) - переводит все символы в противоположный регистр
# upper() - переводит все в верхний регистр
# lower() - переводит все в нижний регистр

# text = 'Hello World'
# print(f'Original: {text}')
# print(text.swapcase())
# print(text.upper())
# print(text.lower())

# index(value) - выводит индекс значения value внутри строки
# find(value) - делает тоже самое что и index,но если не нашел value то вернется -1
 

# text = 'Hello my lord.What u think about kill your brother'

# print(text.index('o', -5))
# print(text.index('kill'))
# print(text.find('s'))


