"""
1) Создайте словарь тремя возможными способами.
"""
# dic_ = {'name':'hi'}
# dic_2 = dict(
#     names='hello'
# )
# dic_3 = dict({
#     ("last","bai")
# })
# print(dic_,dic_2,dic_3)
"""
2) Объявите словарь, удалите один из элементов и распечатайте удалённый элемент.
"""
# dic_ = {'name':'hi'}
# removed = dic_.pop("name")
# print(removed)

"""
3) Объявите словарь, добавьте в него новую пару - "ключ: значение" и распечатайте.
"""
# dic_ = {'name':'hi'}
# dic_['last_name'] = 'your'
# print(dic_)
"""
4) Объявите словарь, удалите всего его элементы и распечатайте.
"""
# dic_ = {'name':'hi'}
# removed = dic_.popitem()
# print(removed)


"""
5) Дан словарь, выведите все его ключи.
"""
# dic_ = {'name':'hi',
#         'names':'hel'
#         }
# ls = list(dic_.keys())
# print(ls)
"""
6)  Объявите словарь, сделайте его копию и распечатайте 
"""
# dic_ = {'name':'hi',
#         'names':'hel'
#         }
# print(dic_)
# ls = dic_.copy()
# print(ls)

"""
7) Это меню вашего ресторана (ключ -- название блюда, значение -- стоимость):
• menu = {'Pad Thai': 200, 'Tom Yam': 170, 'Chicken Teriyaki': 250}
• Добавьте в меню новое блюдо 'Fried Rice' и установите стоимость 150
• Вы решили, что 'Tom Yam' слишком дешевый. Установите новую цену для него: 195
• Ваш повар отвратительно готовит 'Pad Thai', поэтому хотите удалить это блюдо.
• Самостоятельно найдите оператор, который удаляет пару “ключ”:”значение”, и удалите 'Pad Thai' из меню.
• Выведите оставшиеся блюда
"""
# menu = {'Pad Thai': 200, 
#         'Tom Yam': 170, 
#         'Chicken Teriyaki': 250}
# menu.update({'Fried Rice':170})
# menu.update({'Tom Yam':195})
# menu.pop('Pad Thai')

# print(menu)

"""
8) Дан словарь, состоящий из элементов типа: слово-синоним. 
Все слова в словаре различны. Выведите синоним для последнего слова.
Пример : {‘hello’: ‘hi’, ‘good’: ‘nice’, ‘price’: ‘cost’} --> cost
"""
# spisok = {"hello": "hi",
#         'good': 'nice',
#          'price': 'cost'}
# last_ = list(spisok.keys())
# last_[2] = 'value'
# print(last_)

"""
9) Создайте три словаря где будут собраны характеристики некоторых животных, 
затем выведите краткое описание животных.
Пример : dog = {‘name’: ‘Lucky’, ‘age’: 5, 'eyes': 'blue' } 
--> This is a dog. His name is Lucky. It has blue eyes. Lucky is 2 years old. 
"""
# dog = {'name': 'Lucky', 'age': 5, 'eyes': 'blue' }
# cat = {'name': 'Sneg', 'age': 2, 'eyes': 'bluetti' }
# frog = {'name': 'Luck', 'age': 54, 'eyes': 'green' }
# print(f"This is a dog. His name is {dog['name']} . It has {dog['eyes']} eyes. Lucky is {dog['age']} years old.")
# print(f"This is a cat. His name is {cat['name']} . It has {cat['eyes']} eyes. Lucky is {cat['age']} years old.")
# print(f"This is a frog. His name is {frog['name']} . It has {frog['eyes']} eyes. Lucky is {frog['age']} years old.")

# писать код здесь

"""
10) Создайте словарь в котором будет содержаться информация о 
факультетах и учениках, ключом будет факультет, а значением список 
с несколькими учениками. 
Используйте одно имя из списка, который является значением у словаря, 
для выведения утверждения об этом ученике.
Пример : {'Civil Engineering': ['Thomas', 'Benjamin', 'Franklin'], 
'Psycology': ['Joe', 'Chedwick', 'Helena']}
--> This is Franklin. He studies Civil Engineering. 
"""
fac = {
    'Civil Engineering': ['Thomas', 'Benjamin', 'Franklin'], 
    'Psycology': ['Joe', 'Chedwick', 'Helena']
    }
choise = fac['Civil Engineering'][2]
print(f"This is {choise}. He studies Civil Engineering.")


# писать код здесь