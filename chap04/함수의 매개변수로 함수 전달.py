# 함수의 매개변수로 함수 전달하기 
def ten_times(func) :
    for i in range(5):
        func()

def print_hello():
    print("hello")

ten_times(print_hello)

def print_work():
    print('coding')

ten_times(print_work)

#함수 전달의 중요성

def add(x,y) :
    return x+y

def minus(x,y) :
    return x-y

def apply_operation(operation, x, y):
    return operation(x,y)

result = apply_operation(add, 3,4) ## 맵 함수 역활 
result = apply_operation(minus, 3,4)

# 함수도 전달 파라미터 도 전달 

power = lambda x: x*x
under_three = lambda x: x <3
lst= [1,2,3,4,5]

map_list = map(power,lst)
print(f"map() 함수적용 결과 : {list(map_list)}")

filter_list = filter(under_three, lst)
print(f"filter() 함수 적용결과: {list(filter_list)}")

#step 1 함수자체로 인수전달
#step 2 apply-opertainal(add, 3,4) 3,4 전달
#step 3 map 사용
#step 4 람다식 