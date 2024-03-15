# Декоратор - это функция, которая позволяет без изменения кода 
# функции расширить функционал той функции к которой был применен декоратор

import requests
from time import time

# def timeCheckDecorators(func):
#     def wrapper():
#         start = time() #10:26:12
#         func()
#         finish = time() #10:26:32
#         print(f'Time to get result: {round(finish - start, 2)} sec')
#     return wrapper
#     api_url = 'https://api.api-ninjas.com/v1.cars'

# @timeCheckDecorators
# def printCars():
#     car = input('Enter car model: ')
#     api_url = f'https://api.api-ninjas.com/v1/cars?model={car}'
#     response = requests.get(api_url,headers={'X-Api-Key': 'fMvF8LTzSEKonJ8R7LWhEw==GYSkLGG2n8xytyiF'})
#     if response.status_code == 200:
#         print(response.text)
#     else:   
#         print(f'ERROR: {response.status_code} \n{response.text}')
#     return 
# printCars()
# @timeCheckDecorators
# def printUser():
#     api_url = 'https://randomuser.me/api'
#     response = requests.get(api_url)
#     if response.status_code == 200:
#         print(response.text)
#     else:
#         print(f'ERROR: {response.status_code} \n{response.text}')
#     return
# printUser()


# def decorator(func):
#     def wrapper():
#         print('decorator worked!')
#         print(f'{func.__name__} была вызвана')
#         func()
#     return wrapper

# @decorator
# def get_name():
#     print(f'Owner name is John Snow!')
#     return

# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f'Trace: вызвала {func.__name__}()\nона приняла args:{args}, kwargs{kwargs}')
#         res = func(*args,**kwargs)
#         print(f'Trace: vызвала {func.__name__}()\nона вернула: {res}')
#         return res
#     return wrapper

# @trace
# def printAddress(name,address):
#     return f'Name: {name} -> Address: {address}'

# @trace
# def getHello(name,last_name,country):
#     return f'Hello {name} {last_name} from {country}'
# print(printAddress('Din Winchester','kansas'))
# print()
# print()
# print()
# print(getHello('Sam' , last_name='Winchester', country='USA'))

def boldText(func):
    def wrapper(*args,**kwargs):
        res = '<bold>' + func(*args,**kwargs) + '</bold>'
        return res
    return wrapper

def iText(func):
    def wrapper(*args,**kwargs):
        res = '<i>' + func(*args,**kwargs) + '</i>'
        return res
    return wrapper

@iText
@boldText
def get_name():
    name = input('Vvedite svoe name: ')
    return name
print(get_name())