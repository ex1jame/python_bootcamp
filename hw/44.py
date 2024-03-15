


# #-----------------------------------------------------------------



# # Задача: Создание системы учета сотрудников для компании

# # Цель: Разработать классы для управления информацией о сотрудниках в компании, включая их отделы, должности и личные данные.

# # Описание:

# # Класс Employee:

# # Атрибуты: name (имя сотрудника), employee_id (ID сотрудника), position (должность), department (отдел).
# # Методы:
# # Конструктор для инициализации атрибутов.
# # promote(new_position) - повышение сотрудника на новую должность.
# # transfer(new_department) - перевод сотрудника в другой отдел.
# # __str__() - возвращает информацию о сотруднике.

# class Employee:
#     def __init__(self,name,employee_id,position,department) -> None:
#         self.name = name
#         self.employee_id = employee_id
#         self.position = position
#         self.department = department

#     def promote(self,new_position):
#         if new_position == self.position:
#             print(f'{self.name} уже состоит в этой должности')
#         else:
#             self.position = new_position
#             print(f'{self.name} повысили до должности {self.position}')
    
#     def transfer(self, new_department):
#         if new_department == self.department:
#             print(f'{self.name} уже состоит в этом отделе')
#         else:
#             self.department = new_department
#             print(f'{self.name} перевели в отдел {self.department}')
#     def __str__(self) -> str:
#         return f'{self.name} в отделе {self.department} на должности {self.position} и его id {self.employee_id}'

# employee2 = Employee('Raechel',15,'Top-Manager','Marketing')
# employee2.promote('Lead Manager')
# employee2.transfer('Marketing')
# employee3 = Employee('Soska',666,'GEnius','IT')
# employee4 = Employee('nEREALKA',51,'tROYAN','IT')
# # print(employee2)
# # Класс Department:

# # Атрибуты: name (название отдела), department_id (ID отдела), employees (список сотрудников в отделе).
# # Методы:
# # Конструктор для инициализации атрибутов.
# # add_employee(employee) - добавляет сотрудника в отдел.
# # remove_employee(employee_id) - удаляет сотрудника из отдела.
# # get_employees() - возвращает список сотрудников отдела.
# # __str__() - возвращает информацию об отделе и его сотрудниках.
# class Department:
#     def __init__(self,name,department_id) -> None:
#         self.name = name
#         self.dep_id = department_id
#         self.employees = []
    
#     def add_employee(self,employee):
#         return self.employees.append(employee) 
    
#     def remove_employee(self,employee_id1):
#         for empl in self.employees:
#             if empl.employee_id == employee_id1:
#                 self.employees.remove(empl)
#                 return
        
#         return f'Dont have this id'
#     def get_employees(self):
#         return [str(employee) for employee in self.employees]
#     def __str__(self) -> str:
#         return f'{self.name} , id dep {self.dep_id}, spisok {self.employees}'


# employee1 = Department('Marketing',1)

# employee1.add_employee(employee4)
# employee1.add_employee(employee3)
# employee1.add_employee(employee2)
# # employee1.add_employee()
# employee1.remove_employee(15)
# print(employee1.get_employees())


        
        

# # Класс Company:

# # Атрибуты: name (название компании), departments (список отделов в компании), employees (список всех сотрудников).
# # Методы:
# # Конструктор для инициализации атрибутов.
# # add_department(department) - добавляет новый отдел в компанию.
# # add_employee(employee, department_id) - регистрирует нового сотрудника и добавляет его в указанный отдел.
# # find_employee(employee_id) - ищет сотрудника по ID.
# # find_department(department_id) - ищет отдел по ID.
# # transfer_employee(employee_id, new_department_id) - переводит сотрудника в другой отдел.
# # Задание:
# # Реализуйте вышеуказанные классы с соответствующими атрибутами и методами. Создайте взаимодействие между классами
# #  так, чтобы можно было управлять информацией о сотрудниках, их должностях и отделах. Обеспечьте возможность
# #  добавления новых сотрудников и отделов, а также перевода сотрудников между отделами и их повышения в должности.
# class Company:
#     def __init__(self,name_company,employees) -> None:
#         self.name = name_company
#         self.departments = []
#         self.employees =

        
"""Задача: Создание системы учета сотрудников для компании

Цель: Разработать классы для управления информацией о сотрудниках в компании, включая их отделы, должности и личные данные.

Описание:

Класс Employee:

Атрибуты: name (имя сотрудника), employee_id (ID сотрудника), position (должность), department (отдел).
Методы:
Конструктор для инициализации атрибутов.
promote(new_position) - повышение сотрудника на новую должность.
transfer(new_department) - перевод сотрудника в другой отдел.
__str__() - возвращает информацию о сотруднике.



Класс Department:

Атрибуты: name (название отдела), department_id (ID отдела), employees (список сотрудников в отделе).
Методы:
Конструктор для инициализации атрибутов.
add_employee(employee) - добавляет сотрудника в отдел.
remove_employee(employee_id) - удаляет сотрудника из отдела.
get_employees() - возвращает список сотрудников отдела.
__str__() - возвращает информацию об отделе и его сотрудниках.


Класс Company:

Атрибуты: name (название компании), departments (список отделов в компании), employees (список всех сотрудников).
Методы:
Конструктор для инициализации атрибутов.
add_department(department) - добавляет новый отдел в компанию.
add_employee(employee, department_id) - регистрирует нового сотрудника и добавляет его в указанный отдел.
find_employee(employee_id) - ищет сотрудника по ID.
find_department(department_id) - ищет отдел по ID.
transfer_employee(employee_id, new_department_id) - переводит сотрудника в другой отдел.
Задание:
Реализуйте вышеуказанные классы с соответствующими атрибутами и методами. Создайте взаимодействие между классами так, чтобы можно было управлять информацией о сотрудниках, их должностях и отделах. Обеспечьте возможность добавления новых сотрудников и отделов, а также перевода сотрудников между отделами и их повышения в должности."""