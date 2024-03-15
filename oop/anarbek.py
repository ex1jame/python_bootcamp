class Car:
   
    def another_car(self):


        print(f'\n__________{self.model} car_________\n')
        # Car.previous_obj_link = Car.obj_link

    def __init__(self, the_model, the_color, the_year, penalties=0.0):
        self.model = the_model
        self.color = the_color
        self.year = the_year
        self.penalties = penalties
        self.engine_running = False


    def drive(self, city):
        

        if self.engine_running == True:
            print(f'{self.model} is driving to {city}')
        else:
            print('Engine needs a start!')

    def start(self):

        if self.engine_running == False:
            self.engine_running = True
            print(f"The engine of {self.model} has started.")
        else:
            print(f"The engine of {self.model} is already running.")

    def stop(self):
    
        if self.engine_running == True:
            self.engine_running = False
            print(f"The engine of {self.model} has stopped.")
        else:
            print(f"The engine of {self.model} already stopped.")

    def info(self):

        print(f'This is a {self.color} {self.model} from {self.year}.')
    
bmw_car = Car('BMW i8', 'Blue' , 2020)

honda_car = Car('Civic', 'Red', 1995)


def bmw_cars(bmw):
    bmw.another_car()
    bmw.info()
    bmw.start()
    bmw.drive('gosds')
bmw_cars(bmw_car)
bmw_cars(honda_car)
# output

# This is a Blue BMW i8 from 2020.

# The engine of BMW i8 has started.

# BMW i8 is driving to London

# This is a Red Civic from 1995.

# __________another car_________

# This is a Blue BMW i8 from 2020.

