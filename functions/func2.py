# def sum_of_args(a,b,c=5,d=3):
#     return a+b+c+d
# result = sum_of_args(1,2,3,4)
# print(result)

# ----------------------------------
# позиционные и именованные аргументы
# def printParams(a,b,c):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')

# printParams(5,10,15)
# printParams(a=5,c=10,b=15)
# print()

# def sum_of_args(a,b,c,d):
#     return a + b + c + d

# print(sum_of_args(5,10,15,20)) arguments(position arguments)
# print(sum_of_args(b=5,c=10,a=15,d=20)) keyword arguments (name arguments)
# print(sum_of_args(5,10,d=20,c=15))
# ---------------------------------------------
# operator *
# a = [1,2,3]
# b = [4,5,6]
# c = [*a,*b]
# print(c)
# ---------------------------------------------------
# *args, **kwargs 
# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)

# func()

# def printScores(student,*scores):
#     print(f'Name of student: {student}')
#     print(f'AVG: {sum(scores) / len(scores)}')
#     for x in scores:
#         print(f'Score: {x}')   
#         return 5

# printScores('John Snow',100,90,80,70,60,54)

# def printPetNames(owner, **pets):
#     print(f'Owner name: {owner}')
#     print(pets)
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f'{pet}:',*name)
#         else:
#             print(f'{pet}: {name}')
# printPetNames('John Snow',dog='PLuto',cat ='Garfild',fish=['Nemo','Dori','Tima'],turtle = 'Leonardo')


def get_some_data(a,b,*args,**kwargs):
    print('параметры a и b:', a,b)
    print('параметры a и b:', args)
    print('параметры a и b:', kwargs)

get_some_data(1,2,3,4,5, lang='python',car = 'subaru')

# --------------------------------------------------------------
# import string as s
# from random import choice,shuffle
# def generate_random_string(len_):
#     symbols = s.ascii_letters + s.digits
#     res = [choice(symbols) for _ in range(1,len_) ] + [choice(s.punctuation)]
#     shuffle(res)
#     return print(''.join(res))
# generate_random_string(15)
# generate_random_string(4)
# generate_random_string(20)
# generate_random_string(1)
