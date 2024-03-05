class Person:

    def __init__(self,name,age,address,):
        self.name = name
        self.age = age
        self.address = address
        self.weight = [50,100,150,200] #공개 속성
        self.__vision = 1.0 #private 속성

    def __str__(self): #펄슨을 객체 출력시 필요한 것은 
        return "{}\t{}\t{}".format(self.name,self.age,self.address)
            
    
    def show_person_vision(self):
        print("vison is {}".format(self.__vision))
        
new_person = Person('hong',20,'busan')
other_person = Person('kim', 21, 'seoul')


# print(f"bmi = {new_person()}")

print("ths person is {}".format(new_person.name))
print(f"weigth is {new_person.weight}")
# print("vision {}".format(new_person.__vision))
new_person.show_person_vision() #변수.메서드 일반적이다.
print(str(new_person))#str은 함수 객체로 # new_person.str() 이 아닐까. #내추럴 한 코딩
print(new_person.__str__()) # 이것도 가능 

def __len__ (self):
    return len(self.weight)
print(f"weight is {__len__(new_person)}")

my_list=[1,2,3,4]
print(len(my_list))
print(f"list's len is {my_list.__len__()}")

def __call__(self):
    return float(self.weight[1] +self.weight[2] / 2)
print(__call__(new_person))
# def __eq__( self, other):
#     return self.age == other.age

def __getitem__(self,indx):
    return self.weight[indx]

print(f"now is{new_person[2]}")


#객체를 생성하고 함수를 설정하여 티키타카 하면됨
#클래스 변수가 있으면 클래스 메서드가 있다. 잘 사용되지 않는다
# @classmethod ## decorator - 자바 용어는 annotaion






        
