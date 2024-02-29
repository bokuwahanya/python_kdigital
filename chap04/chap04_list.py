for value in range(6):
    print(value)
number = list(range(1,10,2))
print(number)
number_set = {}

squares = [value ** 2 for value in range(1,11)]

    # square = value ** 2
squares.append

print(squares)
print(value)


a = [1,2,3,4,5]
b = [3,4]
c = a + b
print(c)
c1= [x for x in a if x not in b]
c2= list(set(a)-set(b))
print(c1)
print(c2)
 
b = a[:] # 딥카피
a[0] = 100 # 값이 변경되도 딥 카피하면 안바뀜
print(b)

a = [[1,2,3],[4,5,6]]
b = a[:] # : 2차원일 때는 다르다. 1차원가 다르다.
a[0][0] = 100
print(b)

players = ['charles', 'martina', 'michael']
for player in players[:3]:
    print(player.title())

my_foods = ['pizza','falafel','carrot','cake',]
friend_food = my_foods #쉘로우 카피 이름 그대로 들고오면
my_foods.append('cannoli')
print(my_foods)
print(friend_food)

dimensions = (10,20,30,40,50)
#dimensions[0] = 30
print(dimensions)
for dimension in dimensions :
    print(dimension)
dimensions = (200,50)
