# # 1) Умножение соответствующих элементов двух списков: Используйте map и lambda, чтобы умножить соответствующие элементы двух списков.

# print(list(map(lambda x,y:x*y,list(range(1,10)),list((range(1,10))))))

# # 2) Проверка, что в строке есть хотя бы одна гласная буква:
# # Используйте any и lambda, чтобы проверить, что в строке есть хотя бы одна гласная буква.
# print(any(map(lambda x: x in 'aeiouAEIOU', 'dsdsdse')))

# # 3) Фильтрация слов с определенной длиной: Используйте filter и 
# # lambda для фильтрации слов в списке строк, имеющих заданную длину.

# print(list(filter(lambda x:len(x)<=3,['fas','fd','rtes'])))

# # 4) Проверка, что все элементы списка больше нуля: Используйте all и map,
# #  чтобы проверить, что все элементы в списке больше нуля.

# print(all(map(lambda x: x>0,[1,2,0,2,31,4,5])))

# # 5) Сумма квадратов четных чисел: Напишите программу, которая с использованием 
# # map и reduce находит сумму квадратов четных чисел в списке.
from functools import reduce
# print(reduce(lambda y,x:y+x,map(lambda x,:x ** 2 if x % 2 ==0 else 0,range(1,10))))

# Конечно, вот несколько задач, которые вы можете попробовать решить с использованием lambda и reduce в Python:

#     Вычисление суммы квадратов чисел от 1 до n:
#     Напишите программу, используя lambda и reduce, чтобы вычислить сумму квадратов чисел от 1 до n.
# print(reduce(lambda x,y:x+y,map(lambda x :x**2,range(1,int(input('go: '))))))
#     Нахождение наибольшей цифры в числе:
#     Реализуйте программу, которая с использованием lambda и reduce
#  находит наибольшую цифру в заданном числе.
# print(reduce(lambda x,y:x+y,map(lambda x: int(x), (input('go: ').split()))))
print(reduce(lambda x,y:x+y**2,list(map(lambda x:int(x) if int(x) else 5,map(lambda x: x + 1 if x == True else x,any([1,2,3,4,1,1]))))))
#     Объединение строк в предложение:
#     Напишите программу, используя lambda и reduce, чтобы объединить список слов в предложение, добавляя пробелы между словами.

#     Умножение элементов списка на их индексы:
#     Создайте программу, которая с использованием lambda и reduce умножает каждый элемент списка на его индекс.

#     Подсчет количества гласных букв в строке:
#     Используйте lambda и reduce, чтобы подсчитать количество гласных букв в заданной строке.

#     Нахождение произведения положительных чисел в списке:
#     Напишите программу, используя lambda и reduce, чтобы найти произведение всех положительных чисел в списке.

#     Объединение списков строк:
#     Создайте программу, которая с использованием lambda и reduce объединяет несколько списков строк в один.

 