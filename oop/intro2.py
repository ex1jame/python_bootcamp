# class Student:
#     univer = 'MIT'
#     def __init__(self,name)-> None:
#         self.name = name
#         self.books = []
#         self.languages = {}
#         self.knowledge = 0
#         self.is_ready_work = False

#     def  add_points(self, point):
#         self.knowledge +=point
#         if self.knowledge > 500 and not self.is_ready_work:
#             self.is_ready_work=True
#             print(f'{self.name} gets 500 points and is ready to work!')
    
#     def read_book(self, book_name):
#         self.add_points(50)
#         self.books.append(book_name)
    
#     def do_project(self):
#         self.add_points(100)
    
#     def learn_lang(self,language,percent):
#         if percent not in range(70,101):
#             print('Invalid points for lang')
#         else:
#             self.languages[language] = percent
#             self.add_points(percent)

# st1 = Student('John Snow')
# st2 = Student('Din Wichester')

# print(st1.name)
# print(st2.name)

# print(f'Before study {st1.name}: {st1.books}, {st1.languages}, {st1.knowledge}')
# print(f'Ready to work: {st1.is_ready_work}')

# st1.read_book('Grokaev alghoritmy')
# st1.read_book('Grokaev alghoritmy-2')
# st1.read_book('Grokaev alghoritmy-3')

# st1.do_project()
# st1.do_project()

# st1.learn_lang('python',60)
# st1.learn_lang('python',90)
# st1.learn_lang('JS',90)

# st1.do_project()

# print(f'After study {st1.name}: {st1.books},{st1.languages},{st1.knowledge}')
# print(f'Ready to work: {st1.is_ready_work}')\
#------------------------------------------------------------------------------
# class Car:
#     def __init__(self,brand,model) -> None:
#         self.brand = brand
#         self.model = model
    
#     def show_info(self):
#         return f'{self.brand} -> {self.model}'
    
#     def __str__(self) -> str:
#         return f'{self.brand} -> {self.model}'
    
# obj = Car('BMW','8 series')
# print(obj.show_info())
# print(obj)
#-----------------------------------------------------------------------------------
# class Soda:
#     def __init__(self,ingridient = None) -> None:
#         if isinstance(ingridient,str):
#             self.ingridient = ingridient
#         else:
#             self.ingridient = None
    
        