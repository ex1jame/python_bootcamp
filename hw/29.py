"""Функции задания"""

# 1
# Создать функцию, которая будет принимать 3 числа в качестве аргументов, функция должна возвращать сумму первых двух 
# чисел разделеную на третье число
# нужно реализовать проверку на то, что третье число не является нулем, если это ноль, 
# то просто возвратить результат сложения первого и второго числа

# def sum_of_args(a,b,c):
#     sum_ab = a + b
#     if c == 0:
#         return print(sum_ab)
#     else:
#         return print(sum_ab / c)
    
# sum_of_args(2,5,0)
    

# 2
# Создать фуункцию, которая принимает в качестве аргумента список со строками и в каком регистре нужно вернуть данные, 
# строки могут быть записаны в любом регистре, задача: на основе выбора регистра, возвращать либо список 
# со строками в верхнем регистре, либо в нижнем регистре
# Например: func(["hEllo", "wORld"], "lower") -> ["hello", "world"]

# def registr(args,a):
#     conc = ' '
#     for i in args:
#         conc += i
#     if a == 'lower':
#         return print(conc.lower())
#     if a == 'upper':
#         return print(conc.upper())
    
# registr(['hELL','dsadsads'],'upper')


# Создать функцию, которая будет принимать в качестве аргумента строку,
#  а затем говорить сколько в ней и каких символов, результать вернуть в виде объекта
# Например: 'Hello' -> {'H': 1, 'e': 1, 'l': 2, 'o': 1}

# def string_again(string:str):
#     letter_count = {}
#     for letter in string:
#         letter_count[letter] = letter_count.get(letter, 0) +1
#     return print(letter_count)
# string_again('hello')
        
        


# Создать калькулятор используя функции, должны быть доступны операции(+, -, /, *),
#  также должна быть функция-менеджер, которая будет принимать 2 числа и операцию, 
# а затем вызывать нужную функцию и возвращать результат
# def input_calc():
#     num1 = float(input("Введите первое число: "))
#     operator = input("Введите оператор (+, -, *, /): ")
#     num2 = float(input("Введите второе число: "))

#     def calculator_time():
#         nonlocal num1,operator,num2
#         if operator == 'q':
#             print("end")
#         elif operator == '+':
#             result = num1 + num2
#             print(result)
#         elif operator == '-':
#             result = num1 - num2
#             print(result)
#         elif operator == '*':
#             result = num1 * num2
#             print(result)
#         elif operator == '/':
#             # Проверка деления на ноль
#             if num2 != 0:
#                 result = num1 / num2
#                 print(result)
#             else:
#                 print("Ошибка: Деление на ноль недопустимо!")
#                 exit()  # Выход из программы в случае ошибки деления на ноль
#         else:
#             print("Ошибка: Некорректный оператор!")
#             exit()  # Выход из программы в случае ошибочного ввода оператора
#         return exit
#     calculator_time()
# input_calc()

# Создайте функцию, которая будет рассылать сообщения пользователям, сообщая 
# о акции в магазине компьютерной техники, отправлять сообщения нужно только тем людям,
#  которые тем или иным образом относятся к IT-сфере
# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Hel\'ga', 'age': 35, 'work': 'IT-HR' }
# ]
# def newsletter(dictionary):
#     for row in dictionary:
#         for name,work in row.items():
#             if name == 'work' and work.startswith('IT'):
#                 print(f'Hello Mr/Mrs {row["name"]},{work}')
#     return exit()
# print(newsletter(users))


# Создать функцию, которая будет принимать в качестве аргумента 2 строки,
# 1-я строка должна быть следующего вида -> '1200m', вторая строка состоит из величины,
# в которую необходимо преобразовать данные -> 'km', 'cm', 'mm', задача: реализовать
# логику, которая будет принимать например строку вида '2000m', и строку в которую 
# нужно преобразовать величину например 'km', вывод должен быть '2km'
# def dlina_convert(measurement,convert):
#     convet_sym = {'km': 1000, 'cm': 0.01, 'm': 1}
#     symbol_convert =['km','cm','m']
#     for symbol in symbol_convert:
#         if symbol in measurement:
#             measurement = measurement.replace(symbol,'')
#             measurement = float(measurement)
#             converted_measurement = measurement * convet_sym[symbol] / convet_sym[convert]
#             return print(f'Convert values: {converted_measurement} {convert}')

# dlina_convert('1200km','m')



# Создать функцию, которая будет рассчитывать расход топлива автомобиля, 
# будет принимать 2 аргумента 1-й сколько всего километров проехали, второй 
# сколько понадобилось топлива на это, затем функция должна рассчитать сколько ушло 
# топлива на 100 км и вернуть результат вида: 'На 100км было расходовано 10л горючего'
# def fuel_consumption(measurement,fuel):
#     return print(f'На 100 км было расходовано {fuel / measurement * 100} горючего')
# fuel_consumption(500 , 15)




# Расчет премии сотрудникам
# salary- это заработная плата в месяц, 
# overTime- количество часов, которое сотрудник взял сверхурочно, 
# задача: создать функцию, которая будет добавлять к основной зарплате
#  сверхурочное время(1час=200$), функция должна принимать список со словарями
#  и возвращать также список, но уже с измененными данными пример: 
# [{'name': 'Jack', 'salary': 10000, 'overTime': 4}] -> 
# [{'name': 'Jack', 'salary': 10800}]

employees = [
  {'name': 'Jack', 'salary': 10000, 'overTime': 4},
  {'name': 'Tom', 'salary': 15000, 'overTime': 3},
  {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
  {'name': 'Helen', 'salary': 25000, 'overTime': 2},
  {'name': 'Peter', 'salary': 30000, 'overTime': 7}
]
# def salary_bonus(dictionary):
#     for row in dictionary:
#         for name,work in row.items():
#             if name in 'overTime':
#                 bonus_work = work * 200
#         row['salary'] += bonus_work
#         row.pop('overTime')
#     print(dictionary)
#     return  exit()
# print(salary_bonus(employees)) 

# второе решение
# def salary_bonus(dictionary):
#     for row in dictionary:
#         bonus_work = row['overTime'] * 200
#         row['salary'] += bonus_work
#         del row['overTime']
#     return dictionary

# print(salary_bonus(employees))



# Создать функцию, которая в качестве аргумента будет принимать список со
#  строками и числами, задача, отсортировать числа в отдельный список, 
# а строки в отдельный и распечатать оба списка
# def list_StringAndDigits(list):
#     string_list = []
#     digit_list = []
#     for char in list:
#         if isinstance(char,str):
#             string_list.append(char)
#         if isinstance(char,int):
#             digit_list.append(char)
#     return print(digit_list,string_list)
# list_StringAndDigits([1,23,4,4536,45.2,'he','task,',45])






# Создайте функцию, которая будет в качестве аргумента принимать 
# список такого вида как указан выше, и будет возвращать отсортированный 
# список (сортировать по убыванию оценок, используйте sort())
# students = [
#   {'student': 'Jack', 'marks': 43},
#   {'student': 'Tom', 'marks': 92}, 
#   {'student': 'Helen', 'marks': 85}, 
#   {'student': 'Peter', 'marks': 58},
#   {'student': 'Jessica', 'marks': 78}
# ]
# def students_list(dictionary):
#     sorted_students = sorted(dictionary, key=lambda x: x['marks'], reverse=True)
#     return print(sorted_students)
# students_list(students)



# Создайте функцию, которая будет принимать строку, 
# а затем будет смотреть на все товары и возвращать только те, 
# у которых в названии есть данная строка (учесть, что название
#  может быть полным, а может быть частичным)
products = [
  {
    'title': 'Samsung S10', 
    'price': 800, 
    'count': 6, 
    'category': 'samsung'},
  {
    'title': 'iPhone 13 Pro', 
    'price': 1200, 
    'count': 9, 
    'category': 'apple'},
  {
    'title': 'Xiaomi Mi 10', 
    'price': 500, 
    'count': 2, 
    'category': 'xiaomi'},
  {
    'title': 'Samsung S9', 
    'price': 600, 
    'count': 4, 
    'category': 'samsung'},
  {
    'title': 'iPhone 11', 
    'price': 850, 
    'count': 1, 
    'category': 'apple'}
]
# def find_marks(products,string):
#     find_result = []
#     for row in products:
#         for key,value in row.items():
#             if key == 'category' and string in value:
#                 find_result.append(row)
#     return print(find_result)
# find_marks(products,'sa')
# Используя из предыдущей задачи список с товарами, 
# реализовать фильтрацию по категориям, функция должна
# в качестве аргумента принимать строку с категорией и
#  возвращать список, в котором будут только те товары,
#  у которых категория полностью совпадает с переданной



# 13
# Создать счетчик расходов, есть некая переменная, которая будет хранить 
# данные о вашем балансе, создать две функции, первая будет записывать расходы, 
# вторая просто пополнять баланс, первая функция: ее основная задача получать 2 
# аргумента на что потрачено и сколько потрачено, дальше формировать словарь типа: 
# {'target': 'Products', 'spend': 400}, затем сохранять эти данные в список и 
# соответственно вычитать из баланса сумму трат, вторая функция просто получает в 
# качестве аргумента сумму, которую нужно добавить на баланс, также необходимо реализовать 
# проверку, достаточно ли средств на балансе для совершения расходов
while True:
    balance_user= 10200
    def replenish_balance():
        global balance_user
        user_replenish = input('Вы хотите баланс,если да то напишите число для пополнения:')
        if user_replenish == 'q':
            return
        elif user_replenish == 'Все':
            return exit()
        else:
            user_replenish = int(user_replenish)
            balance_user += user_replenish
            print(balance_user)
    def targets_spent():
        global balance_user
        target_data = input('Введите на что вы потратили: ')
        spend_data = int(input('Сколько вы потратили: '))
        if balance_user < spend_data:
            print('Закончились деньги ты бомж')
            return exit()
        products_data = {}
        products_data['target'] = target_data
        products_data['spend'] = spend_data
        ls_data_spent = []
        ls_data_spent.append(products_data['spend'])
        for num in ls_data_spent:
            balance_user -= num
            print(balance_user)
        return 
    replenish_balance()
    targets_spent()


# 14
# Дан пустой список, необходимо использовать его в качестве базы данных для словарей типа 
# {title: 'str', price: num, category: 'str'}, задача реализовать полный 
# CRUD(create(должна быть возможность создавать данные, в нашем случае объекты),
#  read(возможность получения/чтения данных), update(изменение данных(можно использовать 
# индекс)), delete(удаление данных(можно использовать индекс))), за каждое действие должна
#  отвечать отдельная функция
import tkinter as tk
database = []
changes_log = []
def track_changes(func):
    def wrapper(*args, **kwargs):
        global changes_log
        before_change = database.copy()  # Сохраняем состояние до изменения
        result = func(*args, **kwargs)   # Вызываем функцию
        after_change = database.copy()   # Сохраняем состояние после изменения
        # Записываем изменение в лог
        changes_log.append({
            'function': func.__name__,
            'before_change': before_change,
            'after_change': after_change
        })

        return result

    return wrapper
@track_changes
def create_table():
    global database
    database_dict = {name: value for name, value in zip(['title', 'price', 'category'], input('Введите название товара, сумму и категорию через пробел: ').split())}
    database.append(database_dict)
    return

@track_changes
def update_database(database):
    index_dict = int(input('В каком словаре хотите изменить информацию:'))
    keys_dict = input('Что вы хотите изменить title,price,category: ')
    value_dict = input('Напишите новую инфу: ')
    database[index_dict][keys_dict] = value_dict
    return 
@track_changes  
def delete_database(database):
    index_dict = int(input('В каком словаре хотите изменить информацию:'))
    keys_dict = input('Что вы хотите изменить title,price,category: ')
    value_dict = ''
    database[index_dict][keys_dict] = value_dict
    return 
@track_changes
def read_database():
    return print(database)
create_table()
read_database()
update_database(database)
delete_database(database)

print("Изменения в логе:")
for change in changes_log:
    print(change)
root = tk.Tk()
root.title("Tkinter Database App")

# Ввод данных для create_table
create_label = tk.Label(root, text="Введите название товара, сумму и категорию через пробел:")
create_entry = tk.Entry(root)
create_button = tk.Button(root, text="Добавить в базу данных", command=lambda: create_table(create_entry))

create_label.pack()
create_entry.pack()
create_button.pack()

# Ввод данных для update_database
update_index_label = tk.Label(root, text="Индекс словаря для изменения:")
update_index_entry = tk.Entry(root)
update_key_label = tk.Label(root, text="Ключ (title, price, category):")
update_key_entry = tk.Entry(root)
update_value_label = tk.Label(root, text="Новое значение:")
update_value_entry = tk.Entry(root)
update_button = tk.Button(root, text="Обновить базу данных", command=lambda: update_database(update_index_entry, update_key_entry, update_value_entry))

update_index_label.pack()
update_index_entry.pack()
update_key_label.pack()
update_key_entry.pack()
update_value_label.pack()
update_value_entry.pack()
update_button.pack()

# Ввод данных для delete_database
delete_index_label = tk.Label(root, text="Индекс словаря для удаления:")
delete_index_entry = tk.Entry(root)
delete_key_label = tk.Label(root, text="Ключ (title, price, category):")
delete_key_entry = tk.Entry(root)
delete_button = tk.Button(root, text="Удалить из базы данных", command=lambda: delete_database(delete_index_entry, delete_key_entry))

delete_index_label.pack()
delete_index_entry.pack()
delete_key_label.pack()
delete_key_entry.pack()
delete_button.pack()

# Вывод базы данных
result_text = tk.Text(root, height=10, width=50, state=tk.DISABLED)
result_text.pack()

# Запуск главного цикла
root.mainloop()



"""Comprehensions extra"""
8
"""
Из списка 
list1 = [44,54,64,74,104]
Создайте новый list2, прибавив к каждому числу 6
"""
# list1 = [44,54,64,74,104]
# list2 = list(x+6 for x in list1 )
# print(list2)


9
"""Из списка
list1 = [2, 4, 6, 8, 10, 12, 14]
Создайте новый, внеся туда только те числа квадрат которых больше 50
"""
# list1 = [2, 4, 6, 8, 10, 12, 14]
# list2 = list(x for x in list1 if x**2 > 50)
# print(list2)


10
"""
Из сторки string = "happy birthday!"
Создайте список list_, внесите туда все символы из строки кроме пробела и '!'
 
Вывод:
['h', 'a', 'p', 'p', 'y', 'b', 'i', 'r', 't', 'h', 'd', 'a', 'y']
"""
# string = "happy birthday!"
# list1 = list(x for x in string if isinstance(x,str) and x != ' ' and x!= '!')
# print(list1)

11
"""
Дан словарь:
dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
Используйте его чтобы создать список, из значений внутренних словарей

Вывод:
[3, 45, 23, 9, 12, 89]
"""
# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# list1 = list(element for row,z in dict_.items() for key,element in z.items())
# print(list1)




12
"""
Из списка:
list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
Создайте словарь, занесите только те имена, длина которых больше 4.
Ключами будут имена, а значениями их длины, возведенные  
в квадрат. 

Вывод:
{'george': 36, 'ringo': 25, 'patty': 25, 'cynthia': 49, 'linda': 25}
"""
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# dict_ = {name:len(name)**2 for name in list_name if len(name)>4 }
# print(dict_)



# 13
"""
Дан словарь
dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
Пройдитесь по словарю и добавьте в список только те ключи, значение, которых
в диапазоне от 200 до 5000, добавленные в список ключи должны быть в верхнем регистре.
Нужно использовать comprehension.
"""
# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# list1 = {key:value for key,value in dict_.items() if value>200 and value<5000}
# print(list1)



14
"""
Дан словарь:
dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
Создайте словарь dict2:
- Ключи должны быть те же, что и в первом словаре, но каждый символ 'i' замените на ''
- Значением должно быть количество повторений символа 'i' в этом ключе

Вывод:
{'Sedan': 0, 'SUV': 0, 'Pckup': 1, 'Mvan': 2, 'Vann': 0, 'Sem': 1, 'Bcycle': 1, 'Motorcycle': 0}
"""
# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# dict2 = {key.replace('i',''):key.count('i') for key,value in dict1.items() }
# print(dict2)


15
"""
Из списка 
list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
Создайте новый list2, не добавляя все пустые значения(0, None, [], {}, '') 

Вывод:
[1, 2, 3, 'a', 'abc', 23, [1, 2, 3, 4], {'a': 1, 'b': 2}, 'drf']
"""
# list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
# list2 = [element for element in list1 if element not in(None,[],'',0,{})]
# print(list2)



16
"""
Дан список SPL_Patrons. Каждый его подсписок содержит две части информации
о посетителях библиотеки:
- имя посетителя
- количество книг, которые они одолжили за последний год
Используйте list comprehension, 
чтобы создать список readers имен меценатов, 
которые в прошлом году одолжили более 100 книг


SPL_Patrons = [
['Kim Tremblay', 134],
['Emily Wilson', 42],
['Jessica Smith', 215],
['Alex Roy', 151],
['Sarah Khan', 105],
['Samuel Lee', 220],
['William Brown', 24],
['Ayesha Qureshi', 199],
['David Martin', 56],
['Ajeet Patel',69]
]

Вывод:
['Kim Tremblay', 'Jessica Smith', 'Alex Roy', 'Sarah Khan', 'Samuel Lee', 'Ayesha Qureshi']
"""
SPL_Patrons = [
['Kim Tremblay', 134],
['Emily Wilson', 42],
['Jessica Smith', 215],
['Alex Roy', 151],
['Sarah Khan', 105],
['Samuel Lee', 220],
['William Brown', 24],
['Ayesha Qureshi', 199],
['David Martin', 56],
['Ajeet Patel',69]
]
# readers = [name[0] for name in SPL_Patrons  if name[1] > 100]
# print(readers)

17
"""
Из предыдущего списка SPL_Patrons:
предположим, что посетитель экономит в среднем 11,95 доллара, 
одалживая книгу вместо того, чтобы покупать ее. 
Используйте list comprehension, чтобы создать список saved_amount 
сэкономленной суммы для каждого клиента


Вывод:
[1601.3, 501.9, 2569.25, 1804.45, 1254.75, 2629.0, 286.79, 2378.05, 669.19, 824.55]
"""

# saved_amount = [round(save[1] * 11.95,2) for save in SPL_Patrons if isinstance(save[1],int)]
# print(saved_amount)



18
"""
Используйте comprehensions для создания списка из списков, 
где каждый подсписок состоит из имени пирата и стоимости 
его / ее награбленных мешков с зерном 
(рассчитайте стоимость зерна, предположим, 
что средняя рыночная стоимость мешка зерна составляет 42 доллара, 
но включите только тех пиратов, которые любят попугаев)

prairie_pirates = [
['Tractor Jack', 1000, True],
['Plowshare Pete', 950, False],
['Prairie Lily', 245, True],
['Red River Rosie', 350, True],
['Mad Athabasca McArthur', 842, False],
['Assiniboine Sally', 620, True],
['Thresher Tom', 150, True],
['Cranky Canola Carl', 499, False]
]

Вывод:
[['Tractor Jack', 42000], ['Prairie Lily', 10290], ['Red River Rosie', 14700], ['Assiniboine Sally', 26040], ['Thresher Tom', 6300]]
"""
# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]
# ]
# list1 = [[name,mesh * 42] for name,mesh,loves in prairie_pirates if loves]
# print(list1)

19
"""
По данному ниже словарю, пройдитесь циклом
- Найдите сумму лайков всех пользователей, рейтинг которых выше 3
используйте list comprehension

dict_ = {
    'Sasha': {
        'likes': 23,
        'comments': 2,
        'rating': 4
    },
    'Aliya': {
        'likes': 34,
        'comments': 5,
        'rating': 5
    },
    'Dasha': {
        'likes': 15,
        'comments': 3,
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': 2,
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': 7,
        'rating': 2
    }
}


Вывод:
57
"""
dict_ = {
    'Sasha': {
        'likes': 23,
        'comments': 2,
        'rating': 4
    },
    'Aliya': {
        'likes': 34,
        'comments': 5,
        'rating': 5
    },
    'Dasha': {
        'likes': 15,
        'comments': 3,
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': 2,
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': 7,
        'rating': 2
    }
}

print(sum((items['likes'] for id,items in dict_.items() if items['rating'] > 3)))





20
"""
Используя приведенный словарь dict_, создайте список из id, 
которые хранятся под ключом comments. Берите только те комментарии, 
количество которых больше 3

dict_ = {
    'Dasha': {
        'likes': 15,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
        ],
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
        ],
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
            {'id': 4, 'text': 'some text'},
            {'id': 5, 'text': 'some text'},
            {'id': 6, 'text': 'some text'},
        ],
        'rating': 2
    }
}
Вывод:
[1, 2, 3, 4, 5, 6]
"""

# dict_ = {
#     'Dasha': {
#         'likes': 15,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#         ],
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#         ],
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#             {'id': 4, 'text': 'some text'},
#             {'id': 5, 'text': 'some text'},
#             {'id': 6, 'text': 'some text'},
#         ],
#         'rating': 2
#     }
# }
# print([comment['id'] for user_data in dict_.values() for comment in user_data['comments'] if len(user_data['comments']) >3])


