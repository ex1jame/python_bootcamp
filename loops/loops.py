# Циклы это у нас конструкция которая заставляет блок кода выполняться несколько раз

# while <expression>:
    # <body>


# i = 0
# while i < 10:
#     i += 1
#     print(i)

# smt = 'default'
# while (smt:= input('Vvedite chislo: ')) == 'sd':

#     print(smt)

# i = 1  
# while ((name1 := input('Vvedite name1: ')) != 'john') or \
#     ((name2 := input('vvedi second name: ')) != 'raychel'):
#     print()
#     if i >= 5:
#         print('Stop Cycle')
#         break
#     i += 1
# else:
# #     print('horosh')

# user = {'username':'JohnSnow',
#         'password':'bastard123',}
# i = 3
# while password := input(f'{user["username"]} vvedite parol\': ') != user['password']:
#     i -=1
#     if i == 0:
#         print('Vy zablokirovany!')
#         break
# else:
#     print(f'{user["username"]} vy uspeshno zashli v systemu!')

# ---------------------------------------------


# for <variable> in <iterable object>:
    # <body>


# ls = ['a','hello', 55, 66, 77,True]
# i = iter(ls)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# import random
# dict_ = {}
# for x in range(1,21):
#     dict_.update({x:random.randint(1,50)})

# print(dict_)
# startswith( буква на которое начинается )
# endswith(букава на которое заканчивается)

# ls = ['Tirion','Bilal','John','Sansa','Jamie',
#       'Eddart']
# for x in ls:
#     if x.startswith('J'):
#         continue
#     print(f'Hello Mr {x}!')