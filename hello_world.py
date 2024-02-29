# message = "Hello Python world!"
# print(message)
# print(message.upper())
# first_name='ada'
# last_name='lovelace'
# full_name=f"{first_name} \t{last_name.title()} !"
# print(full_name)
# print('language: \npyton\tjava')
vehicles = ['truck', 'bicycle', 'car', 'bike', 'airplane']
print(vehicles[0].title())
print(vehicles[-3])

vehicles[0] = 'jet'
print(vehicles)

vehicles.append('train')
print(vehicles)

vehicles.insert(2, 'horse' )
print(vehicles)

del vehicles[-1]
print(vehicles)
popped_car =vehicles.pop(3)
print(popped_car)

print(f'the last owned moter was a {popped_car.title()}')

too_expensive = 'airplane'
vehicles.remove(too_expensive)
print(vehicles)
print(f"\n A {too_expensive.title()} is too expesive for me")
vehicles.sort(reverse=True)
print(vehicles)
print(sorted(vehicles, reverse=True))
print(len(vehicles))

for vehicle in vehicles :
    print(vehicles)
    print(f"my car is a {vehicles}")

for vehicle2 in vehicles:
    print('my car\n')
    