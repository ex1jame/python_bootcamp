# Создайте декоратор @logger, который будет выводить имя функции и время 
# выполнения при каждом вызове функции.
from time import time, sleep


# def log(func):
#     def wrapper(*args,**kwargs):
# #             start = time() #10:26:12
#         start_func = time()
#         sleep(1)
#         res = func(*args)
#         finish_func = time()
#         print(f'Function {func.__name__} is worked.Time\'s: {finish_func-start_func}')
#         return res
#     return wrapper
# # return decorator
# @log
# # def test_log():
# #     return print(f'GOOOOOOOOOOOOOOOOOOOOOOO')
# # test_log()
# # Реализуйте декоратор @timer_with_timeout, который будет измерять время
# #  выполнения функции и вызывать исключение TimeoutError, если выполнение 
# # занимает больше определенного времени.
# def timer_with_timeout(func):
#     def wrapper(*args,**kwargs):
#         start_func = time()
#         sleep(1)
#         res = func(*args)
#         finish_func = time()
#         if finish_func - start_func > 1:
#             print(f'Func {func.__name__} is time work {finish_func-start_func}')
#         else:
#             raise TimeoutError
#         return res
#     return wrapper
# @timer_with_timeout
# def test_log():
#     return print(f'GOOOOOOOOOOOOOOOOOOOOOOO')
# test_log()
        


# Реализуйте декоратор @profile, который будет анализировать время выполнения 
# каждого участка кода внутри функции и выводить информацию о времени выполнения
#  каждого участка.
import time

def profile(func):
    def wrapper(*args, **kwargs):
        print(f"imya: {func.__name__}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution vremy: {execution_time} secundys")
        return result
    return wrapper
@profile
def example_funsn():
    time.sleep(1)
    for a in range(10000):
        a = a * 2 
    print("Hello, World!")
example_funsn()
