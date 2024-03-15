# zip(iterables) - она соединяет каждый элемент итерируемых обьектов между собой в тип данных tuple и возвращает итератор

# ls1 = [1,2,3,4]
# ls2 = [100,200,300,400,1234]
# ls3 = ['Hello','World','John','andrew']

# print([x for x in zip(ls1,ls2,ls3)])

# -------------------------------
#all(),any()

#all(iterable) - Возвращает True,если все элементы итерируемого обьекта истина, иначе False
# ls = [[1,2],-5,'stroka',1]
# print(all(ls))

# ip1 = '10.255.12.155'
# ip2 = '10.255.1y.155'

# res = all(x.isdigit() for x in ip2.split('.'))
# print(res) 

#any - Возвращает True если хотябы один элемент истинна
# ls = [0,0,'',None,[],1]
# print(any(ls))

# ignore = ['rm -rf','sudo','reset','poweroff']

# command = input('Vvedite commandu: ')
# if any(x in command for x in ignore):
#     raise Exception("You don't have permissions!")
# print('OK')



# Анонимные функции - lambda(обычные функции только без названия)

# lambda функции могут принимать сколько угодно аргументов, 
# но всегда возвращает одно выражение

# def sum_of_args(a,b):
#     return a + b

# print(sum_of_args(5,6))

# func = lambda a,b:a+b
# print(func(15,2))

# def myFunc(n):
#     def result(num):
#         return num * n
#     return result
# def myFunc(n):
#     return lambda num: num * n


# myDoubler = myFunc(2)
# myTripler = myFunc(3)


# print(myDoubler(50))
# print(myDoubler(45))
# print(myTripler(50))

# dict_ = {'John':1_000_000,'Jame':100000000,'Din':1000000,'Anvar':500,'Sam':152}
# res = sorted(dict_.items(),key=lambda x:x[1])
# print(res)

#enumerate - она пронумеровывает каждый элемент внутри iterable,ее собственным индексом

# ls = ['hello','world','Din','Sam','winchesters']
# print(list(enumerate(ls)))


# ------------------------------------------------------------
# map(function,iterable) -> применяет функцию которую мы передаем ко всем элементам iterable

ls = ['one','two','three','Anvar','4545','Titan']
# res = list(map(str.upper,ls))
# print(res)

# res = list(map(lambda name:f'Hello Mr/Mrs {name}!',ls))
# print(res)

# dict_ = {1:2,3:4,5:6}
# print(dict(map(lambda x: (x[0],str(x[1])),dict_.items())))

#filter(function, iterable) -> применяет ко всем элементам iterable функцию которую 
# мы передали и возвращает итератор с теми элементами для кототрых функция вернула True


# res = []
# for x in ls:
#     if x.isdigit():
#         res.append(x)
# print(res)

# res = list(filter(str.isdigit,ls))
# print(res)

# res = list(filter(lambda x: len(x)>5,ls))

# ls = [
#     {'name':'Python','point':18},
#     {'name':'C++','point':4},
#     {'name':'JS','point':8},
#     {'name':'Java','point':3},
#     {'name':'C#','point':9},
# ]

# res = list(filter(
#     lambda dict_: dict_['point'] >= 8,ls
# ))
# print(res)
# users  = [
#     {'username':'kira','comments':'sds'},
#     {'username':'kira', 'comments':''},
#     {'username':'kira','comments':'sds'}
# ]


# active_users = list(filter(
#     lambda obj: obj['comments'], users
# ))
# inactive_users = list(filter(
#     lambda obj: not obj['comments'], users
# ))
# print(active_users)
# print(inactive_users)

# ----------------------------------------
# names = ['Raychel','Sultan','Aigerim','JOhn','kIRA','BOb']

# res = list(
#     map(lambda x: f'Hello Mr/Mrs {x}',filter(lambda x: len(x) > 5,names))
# )
# print(res)
# Функция Reduce () принимает функцию и последовательность и возвращает одно значение,
#  рассчитанное следующим образом:
# 1. Первоначально функция вызывается с первыми двумя элементами из последовательности,
#  и результат возвращается.
# 2. Затем функция вызывается снова с результатом, полученным на шаге 1, и 
# следующим значением в последовательности. Этот процесс повторяется до тех пор,
#  пока в последовательности не закончатся элементы.
# from functools import reduce

# ls = [1,2,3,4,5]
# sum_= reduce(lambda x,y: x+y,ls)
# res_= reduce(lambda a,b: a*b,ls)
# print(sum_,res_)

from itertools import repeat

from itertools import repeat
from random import choices
from string import ascii_letters, digits
from statistics import mean

symbols = '_()$!%+-@#'
q_pass = int(input('Vvedite kolichestvo paroley: '))

result = {
    f(choices(ascii_letters, k=10),
      choices(digits, k=4),
      choices(symbols, k=2),) 
    for f in repeat(
        lambda a, d, s: ''.join(set(a+d+s)), q_pass)
}
print(result)
print(f'Quantity of password: {len(result)}')
dlina = [len(x) for x in result]
print(f'Average len: {mean(dlina)}')