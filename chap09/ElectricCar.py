# 파이썬 코딩은 글쓰듯 해야한다.


from Car import ElectricCar
import numpy as np
my_leaf = ElectricCar('porche', '911s', 2024, 1000)
print(f"elctro {my_leaf.get_descriptive_name()}")
print("elctro {}".format(my_leaf.get_descriptive_name()))