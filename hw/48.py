# Создайте класс мобильного телефона. Определите атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.

class Phone:
    def __init__(self, imei, info_oc) -> None:
        self.__imei = imei
        self.__battery = 100
        self.__info_oc = info_oc

    @property
    def imei(self):
        return self.__imei

    @property
    def battery(self):
        return self.__battery
    
    @battery.setter
    def battery(self,value):
        self.__battery = value 


    @property
    def info_oc(self):
        return self.__info_oc

    def charge_battery(self):
        self.__battery = 100 

    def _consume_battery(self, percentage):
        if self.battery <= 0:
            raise Exception("Your phone is out of power")
        else:
            self.battery -= percentage

    def listening_music(self):
        self._consume_battery(5)
        return self.battery
    def look_video(self):
        if self.battery <= 10:
            print(f'Вы не можете просматривать видео. Заряд батареи: {self.battery}')
        else:
            self._consume_battery(7)
        return self.battery
    
    def __str__(self) -> str:
        self._consume_battery(0.5)
        return f'IMEI: {self.imei} oc: {self.info_oc} {self.battery}'

# Пример использования
phone = Phone(1512354, 'ijgfsdigmf')
print(phone.imei)
print(phone.look_video())
print(phone.listening_music())
print(phone)
