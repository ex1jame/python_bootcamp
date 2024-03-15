# Напишите простое приложение Todo, целью которого является ведение
#  списка дел. Приложение должен состоять из двух классов: Todo и TodoItem:

# Инициализатор Todo ничего не принимает. 
# В классе должен быть метод add_todo, который принимает экземпляр класса 
# TodoItem, и добавляет в список todo_items. Метод list_items должен показывать 
# все элементы в списке todo_items. Метод find должен принимать слово в качестве 
# аргумента и выводить список экземпляров TodoItem, которые содержат это слово в 
# виде кортежа, который будет иметь формат (индекс, экземпляр).
# 

# Инициализатор TodoItem принимает строковое значение.
#  В нем должна быть переменная, сохраняющая состояние is_done. Также
#  в классе должен быть методы check и uncheck, которые меняют состояние is_done.

# Создайте экземпляр Todo, создайте несколько TodoItem, вызовите их методы.

# Сделайте так, чтобы приложение работало с командой строки. 
# Подсказка: в качестве меню может выступать словарь,
#  в котором ключем будет номер, значением -- метод. Для этого можете добавить метод 
# run, в котором будет цикл while принимающий input.


# - Добавить БД в виде файла 
# - Добавить БД в виде PostgreSQL 
# - Добавить в гит

class TodoItem:
    def __init__(self,task) -> None:
        self.task = task
        self.is_done = False
    
    def check(self):
        self.is_done = True
    
    def uncheck(self):
        self.is_done = False


class Todo:
    def __init__(self) -> None:
        self.todo_items = []
    

    def add_todo(self,task):
        self.todo_items.append(task)
    
    def list_items(self):
        return self.todo_items
            
    def __str__(self) -> str:
        return self.todo_items
    
    def find(self,item):
        return [i for i in self.todo_items if item in i.task]
    
    

# Пример использования
todo_list = Todo()

todo_list.add_todo(TodoItem("Погулять с собакой"))
todo_list.add_todo(TodoItem("Сделать покупки в магазине"))
todo_list.add_todo(TodoItem("Почистить квартиру"))
todo_list.add_todo(TodoItem("Позвонить другу"))

# Отмечаем первый элемент как выполненный
todo_list.todo_items[0].check()

# Выводим список задач
print("Список задач:")
print(todo_list.list_items())

# Поиск задач, содержащих слово "покупки"
print("\nПоиск задач, содержащих слово 'покупки':")
found_items = todo_list.find("покупки")
for a in Todo
for index, item in found_items:
    print(f"{index}. [{ 'x' if item.is_done else ' ' }] {item.task}")