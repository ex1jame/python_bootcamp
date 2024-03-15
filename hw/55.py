"""
1. Напишите класс MyList, который наследуется от list. Сделайте так, чтобы индексация
элементов начиналась с 1. Например:
x = MyList([1,2,3,4,5])
x[1] → 1
"""
class MyList(list):
    def __getitem__(self, item):
        if isinstance(item, int) and item >= 0:
            return super().__getitem__(item - 1)
        else:
            raise IndexError('index может быть токо позитивчик')
x = MyList([1,2,3,4,5])
print(x[5])

"""
2. Напишите класс Word и переопределите методы 'больше чем', 
'меньше чем', 'больше или равно', 'меньше или равно' 
для сравнения объектов класса - строк по длине(len). 
Также в методе new напишите условие для удаления
пробелов и пустых строк в созданных словах.
"""
# class Word(str):
#     def __new__(cls, obj):
#         obj = obj.replace(' ', '')
#         return super().__new__(cls, obj)

#     def __init__(self, obj):
#         super().__init__()
#         self.obj = obj
        
#     def __gt__(self, other):
#         return len(self) > len(other)
    
#     def __lt__(self, other):
#         return len(self) < len(other)
    
#     def __ge__(self, other):
#         return len(self) >= len(other)
    
#     def __le__(self, other):
#         return len(self) <= len(other)
    
    

# obj1 = Word('hee1lp')
# obj2 = Word('hepsd')
# print(obj2>obj1) # True
# print(obj1<obj2) # False
# print(obj2>=obj1) # True
# print(obj1<=obj2) # False


"""

3. Создайте класс BankAccount, представляющий банковский счет
. Реализуйте магические методы init, str, add и sub, чтобы поддерживать
 инициализацию счета, вывод информации о счете и операции пополнения и снятия средств.
"""
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'Bank account of {self.name}, balance={self.balance}'

    def add(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def sub(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            return True
        else:
            return False


acc1 = BankAccount("Ivan Ivanov", 500)
print(acc1)  # Output: Bank account of Ivan Ivanov, balance=500

acc1.add(100)
print(acc1)  # Output: Bank account of Ivan Ivanov, balance=600

acc1.sub(100)
print(acc1)

acc1.sub(700)
print(acc1)
