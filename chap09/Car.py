class Car:

    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=100
       
    
    def get_descriptive_name(self):
        long_name= (f"{self.make} {self.model} {self.year}")
        return long_name.title()
    def read_odometer(self):
        print(f"lets go porche {self.odometer}")

    def update_odometer(self, mileage) :
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print('stop')

    def increment_odometer(self, miles):
        self.odometer += miles
    

my_new_car = Car('porche','911',2022)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer = 23
my_new_car.read_odometer()
my_new_car.update_odometer(111)
my_new_car.read_odometer
my_new_car.increment_odometer(23_500)
my_new_car.read_odometer


class ElectricCar(Car) :
    def __init__(self, make, model, year,battery):
        super().__init__(make, model, year)
        self.battery_size= battery
    
    def describe_battery(self):
        return(f"this car battery charge is {self.battery_size}")
    
    def get_descriptive_name(self):
        return super().get_descriptive_name()
        
my_leaf = ElectricCar('nissan','leaf',2024, 200)
print(f" {my_leaf.get_descriptive_name()} battery : {my_leaf.describe_battery()}")
my_leaf.get_descriptive_name()

my_car =Car('bentz','E2200', 2023)
print(f"{my_car.get_descriptive_name()} {my_leaf.describe_battery()}")
    