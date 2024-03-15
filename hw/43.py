"""
1. Создайте класс BankAccount, в конструкторе которого определена переменная
экземпляра класса balance = 0. Определите метод withdraw с параметром amount,
который будет отнимать сумму от баланса и возвращать текущий баланс. Также
добавьте метод deposit, который также имеет параметр amount и соответсвенно
добавляет сумму к балансу, возвращает баланс.
"""
# class BankAccount:
#     def __init__(self,balance = 0) -> None:
#         self.balance = balance
    
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print(f'Amount of purchase: {amount}, remaining balance: {self.balance}')
#         else:
#             print('no money honey')

#     def deposit(self, amount):
#         self.balance += amount
#         print(f'Deposit amount: {amount}, new balance: {self.balance}')

# obj = BankAccount(1000)
# obj.withdraw(900)
# obj.withdraw(900)
# obj.deposit(2000)
"""
2. Вам дан такой код:

winner1 = Nobel("Литература", 1971, "Пабло Неруда")
print(winner1.category, winner1.year, winner1.winner)
print(winner1.get_year())

winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
print(winner2.category, winner2.year, winner2.winner)
print(winner2.get_year())



который выводит в терминал такие значения:

Литература 1971 Пабло Неруда
выиграл 50 лет назад

Литература 1994 Кэндзабуро Оэ
выиграл 27 лет назад

Напишите класс Nobel и метод класса get_year() таким образом, чтобы 
данный вам код вывел указанные значения в терминале. Даты внутри класса не хардкодить.
"""
# class Nobel:
#     def __init__(self,category,year,winner) -> None:
#         self.category = category
#         self.year = year
#         self.winner = winner
    
#     def get_year(self):
#         return f'выиграл {2024 - self.year} лет назад'

# winner1 = Nobel("Литература", 1971, "Пабло Неруда")
# print(winner1.category, winner1.year, winner1.winner)
# print(winner1.get_year())

# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
# print(winner2.category, winner2.year, winner2.winner)
# print(winner2.get_year())
        
"""
3. Создайте класс Password, экземеплярами класса являются пароли в виде строк. 
У класса должен быть метод validate для валидации пароля:
- пароль должен быть минимум 8 символов, но меньше 15
- пароль должен содержать цифры
- пароль должен содержать буквы
- пароль должен содержать хотя бы один из символов:
    '@', '#', '&', '$', '%', '!', '~', '*'

если одно из условий не выполнено, выводите кастомное исключение, 
если же все условия выполнены метод validate должен возвращать строку: 'Ваш пароль сохранен'.

Также переопределите метод str, чтобы при попытке распечатать
сам пароль, вам выдавалась строка из звездочек,
к примеру пароль - 'joe@123456'
в терминале выйдет - ******
"""
# class Password:

#     def __init__(self,password) -> None:
#         self.password = password
    

#     def validate(self):
#         if len(self.password) >= 8 and len(self.password) <= 15:
#             if any(char.isdigit() for char in self.password):
#                 if any(char.isalpha() for char in self.password):
#                     spec_char ={'@', '#', '&', '$', '%', '!', '~', '*'}
#                     if any(char in spec_char for char in self.password):
#                         return True
#                     else:
#                         print("Пароль должен сожержать хотябы один из символов: '@', '#', '&', '$', '%', '!', '~', '*' ")
#                 else:
#                     print('Пароль дожен содержать букву')
#             else:
#                 print('Пароль должен содержать одну цифру')
#         else:
#             print('Пароль должен быть не меньше 8 символов и больше 15')
    
#     def __str__(self):
#         return '*' * len(self.password)


# password1 = Password("Passw0rd!")
# password2 = Password("joe@123456")


# print("Пароль 1:", password1)
# print("Пароль 2:", password2) 


"""
4. Создайте класс Math, экземпляром которого должно быть число.
У классa Math должно быть 3 метода:
- get_factorial - выводит факториал числа
- get_sum - выводит сумму цифр числа
- get_mul_table - выводит таблицу умножения для числа до 10.
 Создайте экземпляр класса и примените к нему все методы. 
"""

# class Math:
#     def __init__(self,number) -> None:
#         self.num = number
    
#     def get_factorial(self):
#         if self.num < 0:
#             return 'Factorial is not defined     for neg number'
        
#         elif self.num == 0 or self.num == 1:
#             return 1
        
#         else:
#             result = 1
#             for i in range(2 , self.num + 1):
#                 result *= i
#             return result
    
#     def get_sum(self):
#         return sum(int(digit) for digit in str(abs(self.num)))
    
#     def get_mul_table(self):
#         if self.num < 0:
#             return 'Multiplication  table is not defined'
#         else:
#             table = []
#             for i in range(1, 11):
#                 table.append(self.num * i)
#             return table
# math_instance = Math(5)

# factorial_result = math_instance.get_factorial()
# print(f"The factorial of {math_instance.num} is: {factorial_result}")

# sum_result = math_instance.get_sum()
# print(f"The sum of digits in {math_instance.num} is: {sum_result}")

# mul_table_result = math_instance.get_mul_table()
# print(f"The multiplication table for {math_instance.num} is: {mul_table_result}")



"""
5. Создайте класс ToDo, экземплярами данного класса являются строки-задачи(сходить в кино, сделать домашку, выгулять собаку и.т.д)

У класса есть метод give_priority который записывает вашу задачу в список(переменная класса) с ключом в виде числа, 
приоритет который вы даете вашей задаче -
к примеру {3: 'сходить в кино'}
приоритет сходить в кино у вас не самый высокий.

У класса должен быть метод list_of_tasks, который выдает вам список отсортированных задач 
по приоритету:
[(1, 'сделать домашку'), (2, 'выгулять собаку'), (3, 'сходить в кино')]

"""

# class Todo:
#     tasks = {}
#     def give_priority(self, task, priority):
#         Todo.tasks[priority] = task

#     def list_of_tasks(self):
#         sorted_tasks = sorted(Todo.tasks.items())
#         return sorted_tasks

# obj = Todo()

# obj.give_priority('сходить в кино',3)
# obj.give_priority('поехать на бали',4)
# obj.give_priority('понюхать кокс',5)

# sorted_task = obj.list_of_tasks()
# print('List of tasks: ',sorted_task)







class Employee:
    def __init__(self, name, employee_id, position, department):
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.department = department

    def promote(self, new_position):
        self.position = new_position
    def transfer(self, new_department):
        self.department = new_department
    
    def __str__(self):
        return f'{self.name}(id: {self.employee_id}) is {self.position} at {self.department}- department'


# print(em1)

class Department:
    def __init__(self, name, department_id, employees = []):
        self.name = name
        self.dep = department_id
        self.empl = employees

    def add_employee(self, employee):
        self.empl.append(employee)

    def remove_employee(self, employee_id):
        for employee in self.empl:
            if employee.employee_id == employee_id:
                self.empl.remove(employee)

    def get_employees(self):
        return f'{self.empl}'
    
    def __str__(self):
        return f'{self.name}(id: {self.dep}) has employees({[i.name for i in self.empl]})'


class Company:
    def __init__(self, name, employees=[], departments=[]) -> None:
        self.name = name
        self.empl = employees
        self.departments = departments

    def add_department(self, department):
        self.departments.append(department)

    def add_employee(self, employee, department_id):
        if self.departments:
            for dep in self.departments:
                if dep.dep == department_id:
                    dep.add_employee(employee)
                    self.empl.append(employee)
        else:
            return 'Такого отдела нет!'
    
    def find_employee(self, employee_id):
        if self.empl:
            for emp in self.empl:
                if emp.employee_id == employee_id:
                    return emp.name
        else:
            return 'Такого сотрудника нет!'  
        

    def find_department(self, department_id):
        if self.departments:
            for dep in self.departments:
                if dep.dep == department_id:
                    return dep.name
                
        else:
            return 'Not found department!'
    
    def transfer_employee(self, employee_id, new_department_id):
        if self.empl:
            for em in self.empl:
                if em.employee_id == employee_id:
                    for dep in self.departments:
                        if dep.dep == new_department_id:
                            em.transfer(dep)
        else:
            return 'Not found employe!'
        
    def __str__(self) -> str:
        return f'Все сотрудники -> {[[i.name, i.department.name]   for i in self.empl]}\nВсе департаменты -> {[i.name for i in self.departments]}'


        


it = Department('IT', 1)
marketing = Department('Marketing', 2)
clining = Department('Clining', 3) 


altai = Employee('Altai', 1, 'boss', clining)
anarbek = Employee('Anarbek', 2, 'boss', marketing)
temirlan = Employee('Temirlan', 3, 'boss', it)


codify = Company('Codify')

codify.add_department(it)
codify.add_department(marketing)
codify.add_department(clining)

codify.add_employee(altai, 1)


print(codify)
codify.transfer_employee(1, 1)
print(codify)

