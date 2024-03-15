class MusicPlayable:
    def play_music(self,song):
        print(f'Now playing {song}')

class Drawable:
    def draw(self):
        print('.-.')
    
    def draw_3d(self,material):
        print(f'Car was printed in 3d with material {material}')
        

class Car(MusicPlayable):
    def __init__(self, model,year):
        self.__model = model
        self.__year = year
    
    @property
    def model(self):
        return self.__model
    
    @property
    def year(self):
        return self.__year

    def __str__(self) -> str:
        return f"This car is a {self.model}, made in {self.year}"

class FuelCar(Car):
    __total_fuel = 1000


    @staticmethod
    def get_fuel_type():
        print('A1-98')

    @classmethod
    def get_total_fuel(cls):
        print(cls.__total_fuel)
    
    @classmethod
    def fill_fuel(cls):
        cls.__total_fuel = 1000
    
    def __init__(self, model, year,fuel_bank):
        super().__init__(model, year)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= fuel_bank
    
    @property
    def fuel_level(self):
        return self.__fuel_bank
    
    
    def __str__(self) -> str:
        return super().__str__() + f' fuel bank: {self.fuel_level}'

    
class Car3D(Car, Drawable):
    def __init__(self, model, year,color):
        Car.__init__(self,model, year)
        self.color = color
        # Calling parent constructor using super() keyword
        MusicPlayable.__init__(self)
    
    def __str__(self):
        return super().__str__() + f' {self.color}'

# Testing the code




c1 = Car("Tesla Model S",2021)
print(c1)
# c1.play_music("Song")

c3d = Car3D("Model X",2025,'Red'  )

print(c3d)
c3d.draw()
c3d.draw_3d('Metal')

mustang_car = FuelCar('Mustang',2021,60)
print(mustang_car)

FuelCar.get_total_fuel()
# FuelCar.get_total_fuel -= 100
FuelCar.get_total_fuel()
FuelCar.get_fuel_type()
