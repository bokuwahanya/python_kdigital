class Vehicle:

    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    
    def get_decribe_name(self):
        return (f"{self.make} {self.model} {self.year}")
     
My_vehicle = Vehicle("porche","911",2024)
print(My_vehicle.get_decribe_name())

class Electirc(Vehicle):
    def __init__(self, make, model, year, battery):
        super().__init__(make, model, year)
        self.battery=battery

    def get_decribe_battery(self):
        return(f" battery charge : {self.battery}")
    
my_car = Electirc('nissan',"gtr",2024, 10000)
print (f"{my_car.get_decribe_name()} {my_car.get_decribe_battery()}")
