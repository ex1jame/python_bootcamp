# Автомобиль: создайте класс с именем Car. Метод __init__ () класса Car должен содержать 
# три атрибута: brand, year и color. Создайте метод get_auto(), который выводит информацию 
# об автомобиле, и метод get_year, который выводит возраст авто .

# Добавьте атрибут horsepower, который равен 85.

# Напишите метод add_horsepower, который всем машинам будет добавлять по 20 л/с,
#  а машинам Mers, Bmw, Poshe по 40 л/с

# Создайте на основе своего класса экземпляр с именем bmw . Выведите три атрибута 
# по отдельности, затем вызовите все методы.

# Два авто: начните с класса из вышеописанного упражнения. Создайте 2 разных экземпляра,
#  вызовите для каждого экземпляра метод get_auto

# Студенты: создайте класс с именем Student. Создайте атрибуты name, age, course. 
# Напишите метод get_student(), который выводит сводку с информацией о студенте .
#  Создайте еще один метод get_birth_year() для вывода информации о годе рождения студента.

# Создайте несколько экземпляров, представляющих разных студентов. Вызовите оба метода
#  для каждого студента.


class Car:
    horsepower = 85
    def __init__(self,brand, year,color) -> None:
        self.brand = brand
        self.year = year
        self.color = color
    
    def get_auto(self):
        print(f'Brand -> {self.brand} \n Year -> {self.year} \n Color -> {self.color}')
    
    def get_year(self):
        print(f'Year auto --> {2024 - self.year}')
    
    def add_horsepower(self):
        if self.brand in ('Mers,Bmw,Poshe'):
            self.horsepower += 40
            print(self.horsepower)
        else:
            self.horsepower += 20
            print(self.horsepower)



bmw = Car('Bmw',2003,'black')
honda = Car('Honda',2001,'white')
honda.get_auto()
bmw.get_auto()
bmw.get_year()
bmw.add_horsepower()


# Студенты: создайте класс с именем Student. Создайте атрибуты name, age, course. 
# Напишите метод get_student(), который выводит сводку с информацией о студенте .
#  Создайте еще один метод get_birth_year() для вывода информации о годе рождения студента.

# Создайте несколько экземпляров, представляющих разных студентов. Вызовите оба метода
#  для каждого студента.

class Student:
    def __init__(self,name,age,course) -> None:
        self.name = name
        self.age = age
        self.course = course

    def get_student(self):
        print(f'NAME --> {self.name}\nAge --> {self.age}\nCourse --> {self.course}')
    
    def get_birth_year(self,birth):
        print(f'{self.name} of birthday --> {birth}')


student1 = Student('Adam',25,'Software Eng')
student2 = Student('Susan',19,'Software Eng')
student3 = Student('Caisy',21,'Software Eng')

student1.get_student()
student2.get_student()
student3.get_student()
student1.get_birth_year('20-01-1998')