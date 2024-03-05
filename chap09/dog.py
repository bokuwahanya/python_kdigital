class Dog:

    def __init__(self, name, age, price):
        self.name= name #-> 생성된 객체 ->자기자신 #속성 > 자바의 클래스 field
        self.age = age #->resive 오브젝  
        self.__price = price
        #자바에서 보던 field에 데이터 할당

    
    def sit(self) :
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        print(f"{self.name} rolled over!")
#클래스 안에서 접근할때는 self.name

my_dog = Dog('whille', 6, 100)#생성자 호출_>인스턴스 새성 >__init__함수 : 이게 self
my_dog.sit() # 저위의 sit의 self는 my_dog를 가르킴 
print(f"dog's name is {my_dog.name} {my_dog.__price}")
#self의 전달이 눈에 보이지 않는다. 주의 

#클래스 밖에서 접근할때는 변수명.name