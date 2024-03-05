class Restaruant :
    def __init__(self, rname, rtype) :
        self.restaurant_name=rname
        self.cuisine_type=rtype

    def describe_resturant(self):
        print(f"Restaruant {self.restaurant_name} is good")
    
    def open_restaurnat(self):
        print(f"today {self.cuisine_type}")
new_rest = Restaruant('umai', 'sushi')
new_rest.describe_resturant()
new_rest.open_restaurnat()

class Icecreamshop(Restaruant):
    def __init__(self, name, ctype, flavors):
        super().__init__(name, ctype)
        self.flavors=flavors

    def show_flavors(self):
        return(f"today's flavor is {self.flavors}")


    flavors = ["chocolete"]
new_Ice = Icecreamshop('kikat','ice cream','milk')
    

print(f"{new_Ice.flavors} is one of the best japan {new_Ice.show_flavors()} Restaruant")      