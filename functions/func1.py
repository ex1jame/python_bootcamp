    # # Найти квадрат,куб,результат деления на 100 любых 3 чисел

    # # num = 5
    # # dict_ = {
    # #     'num':5,
    # #     '2':25,

    # # }
    # # num1 = 5
    # # num2 = 75
    # # num3 = 1154
    # # res = {'num':num1, '2':num1 ** 2, '3':num1 ** 3,
    # #        '100':num1 /100}
    # # res2 = {'num':num2, '2':num2 ** 2, '3':num2 ** 3,
    # #        '100':num2 /100}
    # # res3 = {'num':num3, '2':num3 ** 2, '3':num3 ** 3,
    # #        '100':num3 /100}
    # # print(res,res2,res3, sep='\n\n')

    # # DRY - Don't repeat yourself

    # # def do_operations(num: int) -> None:
    # #     res = {'num':num, '2':num ** 2, '3':num ** 3,
    # #        '100':num / 100}
    # #     print(res)
    # # print(do_operations(num2))

    # # -------------------------------------
    # # function - это именнованая часть программы которая содержит в себе определенный
    # #  блок кода и может вызываться в других частяx
    # # программы столько раз сколько угодно

    # # def name_of_function(<a, b> параметры функции):
    #     # <body> код, какая то логика которая будет давать конечный результат
    #     # <return> оператор который помогает сохранить результат

    # # name_of_func(4,6 #аргументы)

    # # параметры функции - переменные в которых мы временно сохраняем данные которые передаем при вызове в функцию,
    # #они доступны только внутри функции

    # # аргументы функции - данные которые мы передаем ппм вызове функции,попадают в параметры по очередно


    # # def isEven(num):
    # #     return(True if num % 2 == 0 else False)
        
    # # # 


    # # def isEven(num: int) -> bool:
    # #     """Return True of False after checking number for even!"""
    # #     return True if num % 2 == 0 else False

    # # num1 = 44
    # # print(isEven(num1))

    # # --------------------------------------------------------------
    # # default параметры

    # # def sum_of_args(a: int,b: int,c: int = 0) -> int:
    # #     """Returns sum of given arguments"""
    # #     try:
    # #         return a + b + c
    # #     except TypeError:
    # #         raise Exception('invalid values for arguments')
        
    # # print(sum_of_args(54,23,42))
    # # print(sum_of_args(52,212,4242))
    # # print(sum_of_args(4,2,4))

    # # --------------------------------------------
    # # print(len('string'))
    # # from typing import Iterable

    # # def our_len(obj:Iterable) -> str:
    # #     """Возращает длину итерируемого обьекта"""
    # #     i = 0
    # #     print(obj)
    # #     for _ in obj:
    # #         i +=1
    # #     print(f'result: {i}')
    # # our_len([1,2,3,4,5])
    # # our_len('string is number one bro')

    # # ----------------------------------------------------
    # dsd = 'Hello world! My name is John, last name is Snow. Nice to meet you!'
    # 'you! to meet to Nice Snow. is ...'
    # def reverse_text(text:str) -> str:
    #     '''Reversing text!'''
    #     spisok = text.split()
    #     # return ' '.join(reversed(spisok))
    #     return ' '.join(spisok[::-1])
    # print(reverse_text('Hello world! My name is John, last name is Snow. Nice to meet you!'))