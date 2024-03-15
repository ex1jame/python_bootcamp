
"""Создайте класс Auto в нем реализуйте метод ride который выводит сообщение Riding on a ground, 
создайте класс Boat реализуйте метод swim, который выводит floating on water.
Создайте класс Amphibian который наследуется от класса Auto и Boat. Создайте от него объект и вызовите все методы.
"""
# class Auto:
#     def ride(self):
#         print(f'Riding on a ground')

# class Boat:
#     def swim(self):
#         print(f'floating on water')

# class RadioMixin:
#     def play_music(self,song):
#         print(f'Playing {song}')

# class Amphibian(Auto,Boat,RadioMixin):
#     pass

# obj = Amphibian()
# obj.ride()
# obj.swim()
# obj.play_music('Weekend')

"""Создайте класс RadioMixin в нем реализуйте метод для проигрывания музыки play_music который принимает в себя название песни.
 Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина"""

"""Будильник

Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включатся будильник."""
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
class Clock:
    def time_now(self):
        print(f"Current Time is {current_time}")

class Alarm:
    def __init__(self) -> None:
        self.alarm_set = False
    
    def set_alarm(self):
        self.alarm_set = True
        print('Alarm is set')
    
    def disable_alarm(self):
        self.alarm_set = False
        print('Alarm is disabled')
    

class AlarmClock(Clock,Alarm):

    def set_alarm(self,hour,minute):
        alarm_time = now.replace(hour=hour, minute=minute,second=0,microsecond=0)
        self.alarm_time = alarm_time
        super().set_alarm()
        

obj = AlarmClock()

obj.time_now()
obj.set_alarm(5,10)
# obj.disable_alarm()

"""Разработчики
Напишите класс Coder с атрибутами experience, count_code_time = 0 и абстрактными методами
get_info и coding.
Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder.
 Класс Backend должен принимать дополнительно параметр languages_backend, а Frontend — languages_frontend соответственно.
Переопределите в обоих классах методы get_info и coding (так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time). 
Так же бывают FullStack разработчики и
поэтому создайте данный класс и чтобы у него были атрибуты и методы предыдущих классов. Создайте несколько экземпляров от классов Backend, Frontend, FullStack и вызовите их методы."""

# class Coder:
#     def __init__(self,experience, count_code_time=0) -> None:
#         self.exp= experience
#         self.ct_code = count_code_time
    
#     def get_info(self):
#         print(f'{self.exp} , {self.ct_code}')
    
#     def coding(self):
#         pass

# class Backend(Coder):
#     def coding(self):
#         self.ct_code +=3600

# class Frontend(Coder):
#     def coding(self):
#         self.ct_code +=1800

# class FullStack(Backend,Frontend):
#     def __init__(self, experience, count_code_time=0) -> None:
#         super().__init__(experience, count_code_time)
#     def get_info(self):
#         super().get_info()
#         print("I can code both backend and frontend")

# back = Backend(5)
# front = Frontend(4)
# full = FullStack(10)

# back.coding()
# back.get_info()
# print('-------------------------')
# front.coding()
# front.get_info()
# print('---------------------------')
# full.coding()
# full.get_info()


class Coder:
    def __init__(self, experience):
        self.experience = experience
        self.count_code_time = 0

    def get_info(self):

        raise NotImplementedError("Метод get_info должен быть переопределен в подклассе")

    def coding(self):

        raise NotImplementedError("Метод coding должен быть переопределен в подклассе")


class Backend(Coder):
    def __init__(self, experience, languages_backend):
        Coder.__init__(self, experience)
        self.languages_backend = languages_backend

    def get_info(self):
    
        return f"Backend разработчик с опытом {self.experience} лет, владеющий языками {', '.join(self.languages_backend)}"

    def coding(self, hours):

        self.count_code_time += hours
        return f"{self.get_info()} кодит {hours} часов"


class Frontend(Coder):
    def __init__(self, experience, languages_frontend):
        Coder.__init__(self, experience)
        self.languages_frontend = languages_frontend

    def get_info(self):

        return f"Frontend разработчик с опытом {self.experience} лет, владеющий языками {', '.join(self.languages_frontend)}"

    def coding(self, hours):
        self.count_code_time += hours
        return f"{self.get_info()} кодит {hours} часов"
class FullStack(Backend, Frontend):
    def __init__(self, experience, languages_backend, languages_frontend):
        Backend.__init__(self, experience, languages_backend)
        Frontend.__init__(self, experience, languages_frontend)
    def get_info(self):
        return f"FullStack разработчик с опытом {self.experience} лет, владеющий языками {', '.join(self.languages_backend)} и {', '.join(self.languages_frontend)}"


backend_developer = Backend(5, ['Python', 'Django'])
print(backend_developer.get_info())
print(backend_developer.coding(8))

frontend_developer = Frontend(3, ['JavaScript', 'React'])
print(frontend_developer.get_info())
print(frontend_developer.coding(4))

fullstack_developer = FullStack(8, ['Python', 'Django'], ['JavaScript', 'React'])
print(fullstack_developer.get_info())
print(fullstack_developer.coding(2))