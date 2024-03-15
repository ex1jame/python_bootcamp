# dict() - Словарь -> упорядоченная коллекция элементов(python 3.7 -> ordered). 
# Каждый элемент внутри словаря хранится в виде пары
# --> {ключ: заключения}

# ассоциативный массив, hash table, object(js), structure == dictionary(py)

# ключами могут быть только неизменяемые типы данных и в словаре сохраняются
#  только уникальные ключи
# тогда как значениями могут выступать любые типы данных и любые значения

# thisdict = {
#     'brand':'Ford',
#     'model':'Mustang',
#     'year': 1967
# }
# ls = ['Ford','Mustang',1967]

# print(thisdict, type(thisdict))
# print(ls, type(ls))
# print(thisdict['brand'],thisdict['model'],thisdict['year'],thisdict['brand'])

# thisdict['motor'] = 'GTI Turbo'
# thisdict['model'] = 'fiesta'
# print(thisdict)

# ---------------------------------------------------
# print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 
# 'pop', 'popitem', 'setdefault', 'update', 'values'

# items,keys,values
# user_info = {
#     'first_name':'John',
#     'last_name':'Johnathan',
#     'age': 24,
#     'email' : 'bastard123@gmail.com',
#     'role': 'admin'

# }
# print(user_info)
# ls = list(user_info.keys())
# print(ls)

# ls2 = list(user_info.values())
# print(ls2)

# ls3 = list(user_info.items())
# print(ls3)
# print('\nValues:')
# for value in user_info.values():
#     print(value)
# print('Keys:')
# for key in user_info.keys():
#     print(key)

# for key,value in user_info.items():
#     print(f'keys: {key}, values: {value}')

# изменение
# dict_ = {'name':'Jack','age': 17}
# print(dict_)
# dict_['name'] = 'John'
# dict_['address'] = 'Winterfell'
# print(dict_)
# dict_.update(age=24,address='BlackCastle',gege='sdsd',name='john sdasda')
# print(dict_)
# dict_.update({'name':'Jonh Snow'})
# print(dict_)
# --------------------------------------------
# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_[3], '!!!')
# print(dict_.get(5, 'Not found!')) # index, value

# setdefault - работает так же как get,но если нет такого ключа
# tо создает новую пару из этого ключа
# print(dict_.setdefault(2))
# print(dict_.setdefault(5,'default'))
# print(dict_)
# ---------------------------------------------
# создание - fromkeys
# ls = list(range(1,20))
# new_dict = dict.fromkeys(ls,'default')
# print(new_dict)
# --------------------------------------------
# удаление элементов
# pop,popitem

# pop(<key>) - удаляет пару по ключу
# popitem() - удаляет последнию пару

# dict_ = {'name':'John','last_name':'Snow','last_name':'Sdsds'}
# print(dict_)
# removed = dict_.pop('name')
# print(dict_)
# print(removed)
# print('------------------------------')
# removed = dict_.popitem()
# print(dict_)
# print(removed)
# # -----------------------------------------
# roles = {
#     1: 'Admin',
#     2: 'Customer',
#     3: 'Vendor',
# }

# users = {
#     55:{
#         'id':55 , 'role':roles[3], 'username':'Tirion',
#     },
#     12:{
#         'id':12, 'role':roles[2], 'username':'John',
#     },
#     4:{
#         'id':4 , 'role':roles[1], 'username':'Saranta',
#     }
# }
# print(users[12]) вывести через определенное айди
# print(list(users[12])) выводит список через айди только ключи
# product = {
#     'id': 1,
#     'title' : 'Samsung Galaxy S23 Ultra',
#     'description': 'Lorem ipsum',
#     'price': 100
# }
# print(product)
# id_users = int(input('Vvedite id: '))
# if users[id_users]['role'] == roles[1]:
#     product['description'] = input('Vvedite opisanye: ' )
# else:
#     print('You don\'t have permissions!')
    
# if users[id_users]['role'] == roles[2]:
#     product["price"] = input('Vvedite opisanye: ' )
# else:
#     print('You don\'t have permissions!')
# print()
# print(product)