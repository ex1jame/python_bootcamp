# [Forwarded from Анвар]
# 1) '''Напишите декоратор, который проверяет, что функция вызывается с определенными 
# типами аргументов.'''
# def type_check(definite_arg):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             for arg in args:
#                 if not isinstance(arg,definite_arg):
#                     raise TypeError(f'Argument{arg} is not {func}')
#             res = func(*args,**kwargs)
#             print(f'Function {func.__name__} is worked')
#             return res
#         return wrapper
#     return decorator

# @type_check(str)
# def example_str(string):
#     return print(sorted(string))
# example_str('Hello World')
    
                

# 2) '''Создайте декоратор, который автоматически преобразует результат
# #  функции в другой тип данных,'''
# def convert_result(convert_type):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             result = []
#             for arg in args:
#                 result.append(convert_type(arg))
#             return result
#         return wrapper
#     return decorator

# @convert_result(int)
# def example_int(*args):
#     return args
# print(example_int('515','1515','543','15'))

            


# 3) '''Реализуйте декоратор, который ограничивает максимальное количество вызовов функции.'''

# def limited_calls(max_calls):
# #     def decorator(func):
# #         def wrapper(*args,**kwargs):
# #             nonlocal count
# #             if count < max_calls:
# #                 count += 1
# #                 return func(*args)
# #             else:
# #                 raise ValueError(f'Function{func.__name__} dont work')
# #         count = 0
# #         return wrapper
# #     return decorator

# # @limited_calls(5)
# # def emax_call():
# #     return f'Hellow ty bystryi'

# # print(emax_call())
# # print(emax_call())
# # print(emax_call())
# # print(emax_call())
# # print(emax_call())
# # print(emax_call())


# # 4) '''Напишите декоратор, который автоматически логирует исключения,
# #  возникающие внутри функции.'''
# # def decorator(func):
# #     def wrapper(*args,**kwargs):
# #         try:
# #             res = func(*args)
# #             if float(res):
# #                 print(f'Function is worked yeaaahh')
# #                 return res
# #             else:
# #                 raise ValueError
# #         except ValueError:
# #             f'GG error blyat'

# #     return wrapper
# # @decorator
# # def test_xt(a='5.2'):
# #     return a
# # print(test_xt())
            
# # 5) '''Создайте декоратор, который выполняет аутентификацию пользователя перед
# #  вызовом функции.'''
# users = [
#     {'name':'Sun'},
#     {'name':'Alita'},
#     {'name':'Tima'}
# ]
# def auth_user(user):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             res = func(*args,**kwargs)
#             for col in users:
#                 print(col['name'])
#                 if user in col['name']:
#                     print(f"Function {func.__name__} is worked u pro")
#                     return res
#                 else:
#                     print(f"Dont't have permission")
#                     return
#         return wrapper
#     return decorator
# @auth_user(user = input('Vvedite username: '))
# def user_test(a):
#     return a
# print(user_test('Hello World!'))


# # 6) '''Реализуйте декоратор, который изменяет значение возвращаемого результата функции, 
# # например, умножая его на определенный коэффициент.'''
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         multiplication = list(map(lambda x: x * 2, args))
#         print(f'Function result: {func},Multiplication decorator: {multiplication}')
#         return func(*args,**kwargs)
#     return wrapper

# @decorator
# def func_1(a):
#     return a
# print(func_1(7))


# # 7) '''Напишите декоратор, который ограничивает доступ к функции только
# #  определенным пользователям или ролям.'''
# users = [
#     {'name':'Nasty','roles':'moderator'},
#     {'name':'Anton','roles':'admin'},
#     {'name':'Stark','roles':'user'},
#     {'name':'Tony','roles':'admin'},
# ]
# def user_roles(user_name):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             user = next((u for u in users if u['name'] == user_name),None) 
#             #проверяет есть ли вользователь в словаре и если есть он выводит его в переменную
            
#             if 'roles' in user:
#                 required_roles = user['roles']
#                 if required_roles in user['roles'] and required_roles in ('admin','moderator'):
#                     return func(*args,**kwargs)
#                 else:
#                     raise PermissionError(f"User '{user_name}' doesn't have to permission")
#             else:
#                 raise ValueError(f"User '{user_name}' not found in the user list")
#         return wrapper
#     return decorator

# @user_roles('Anton')
# def admin_func():
#     return f'hello world'
# print(admin_func())
# # 8) '''Создайте декоратор, который преобразует аргументы функции в определенный 
# # формат перед её выполнением, например, в строку в верхнем регистре.'''
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         convert = list(map(str.upper,args))
#         print(f'Function {func.__name__} is converted to str and up {func(*convert)}')
#         return func(*convert)
#     return wrapper

# @decorator
# def test_1(a):
#     return a
# print(test_1('string time'))




# 9) '''Напишите декоратор, который устанавливает максимальное время выполнения функции
#  и завершает её, если оно превышено.'''
# from time import time, sleep
# def max_time(max_chill):
#     def timeCheckDecorators(func):
#         def wrapper(*args,**kwargs):
#             start = time() #10:26:12
#             sleep(1)
#             result = func(*args)
#             finish = time() #10:26:32
#             time_to_check = finish - start
#             print(time_to_check)
#             if max_chill < time_to_check:
#                 print(f'Function {func.__name__} is worked hehe')
                
#             else:
#                 print('Uscorte')
#             return result
#         return wrapper
#     return timeCheckDecorators

# @max_time(1)
# def test_d():
#     return f'Bolot'
# print(test_d())
# 10) '''Напишите декоратор, который ограничивает доступ к функции только
#  в определенное время суток.'''
# from datetime import datetime
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         current_time = datetime.now().time()
#         print(current_time)
#         if 0 <= current_time.hour < 12:
#             return f'Night'
#         else:
#             return func(*args)
#     return wrapper

# @decorator
# def sss():
#     return 'hesoyam'
# print(sss())

# 11) Напишите декоратор, который перехватывает определенные исключения, 
# возникающие в функции, и преобразует их в другие исключения или обрабатывает 
# особым образом.
def decorator(func):
    def wrapper(*args,**kwargs):
        try:
            res = func(*args)
            float(res)
            
        except ValueError:
            raise ZeroDivisionError('переопределение ошибки')

    return wrapper
@decorator
def test_xt(a):
    return a
print(test_xt('hello'))

