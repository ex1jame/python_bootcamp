# list( ) - (списки,массив) - ищменяемый,последовательный тип данныых, который представляет из 
# себя коллецию каких либо объектов(элементы) внутри себя

# my_list = [1, 'string', 'hello', False, None, [1,2,3, [2,4,5, [2]]]]
# print(my_list,type(my_list))

# range( ) - возвращает последовательность чисел
# numbers = range(1, 101)
# print(numbers)
# ls = list(numbers)
# print(ls)

# ls = list('Hello World')
# print(ls)

# Игдексация в списках
# ls = [1,2,3,4,5, 'String', [True,False,None], 5]
# print(ls, len(ls))
# print(ls[5],ls[-1])
# print(ls[6][0]) Вызов массива в массиве
# print(ls[3:6])

# i = 0
# while i < 5:
    # print( i)
    # i += 1

# ls = range(1, 11)
# for num in ls:
    # print(num)
# ls_ti = 'Sansa'
# ls = ['John','Sansa','Tirion', 'Eddart','Jamie']
# for name in ls:
#     if name in ls_ti:
#        print(name)

# for x in ls:
    # print(f'Welcome to the club baby {x}')

# for num in range(1, 21):
#     # print(num)
#     if num % 2 == 0:
#         print(f"Число {num} четное, kvadrat: {num ** 2}")
#     else:
#         print(f"Число {num} нечетное, куб: {num ** 3}")


# ---------------------------------------
 

# методы списков
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
  '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', 
  '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
'__subclasshook__', 'append', 'clear','copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse',
 'sort']
# print(dir([list]))
# append(element) - Добавляет элемент в конец списка
# ls = [1,2,3]
# print(ls)
# ls.append(4)
# ls.append(5)
# ls.append('Hello')
# ls.append([True,False])
# print(ls)

# extend(container) - расширяет список

# ls = [1, 2, 3]
# ls.append('Hello')
# print(ls)
# ls.extend('HEllo')
# print(ls)
# ls.extend([True,False])
# print(ls)

# ls = [1,2,3]
# ls1 = [1,2,3]
# print(ls + ls1)

# sort() - сортирует список, если передать reverse=True,
# то список отсортируется в убывающем порядке
    
# from random import randint

# ls = []
# for a in range(1 , 101):
#     num = randint(1, 100)
#     ls.append(num)
# print(ls)
# ls = list(set(ls))
# ls.sort(reverse = True)
# print('After: \n', ls)


# insert(index, element) - добавляет элемент по указанному index

# ls = ['string',1 ,2 ,3 , False]
# ls.insert(1, 1)
# ls.insert(5, 'hi')
# print(ls)


# remove(element) - удаляет elemnet из списка, если такого нет,выводится ошибка
# pop([index]) - удаляет и возвращает элемент из списка по index, но если index не передать, 
# то удаляет последний элемент
# ls = [ 5, 1, 2, 4, 4, 5, 5, 5]
# print(ls)
# ls.remove(5)
# print(ls)
# while 5 in ls:
#     ls.append(4)
#     ls.remove(5)
# print(ls)
# ls.pop() Удаляет последний индекс
# ls.pop(0) удаляет указанный индекс
# ls = [1, 2, 3]
# deleted = ls.pop()
# print(ls)
# print(deleted)
 

# update------
ls = [1 , 2, 't', 4, 5, 6, None, 8]
ls[2] = 3
print(ls)
i = ls.index(None)
ls[i] = 7
print(ls)
