class Shape:
    def __init__(self,base,height,tall):
        self.__base = base
        self.__height = height # private 변수 
        self.tall = tall

    @property ##decorator for getter
    def get_base(self):
        return self.__base
    
    @property
    def get_height(self):
        return self.__height

    @property
    def set_height(self, value):
        self.__height=value

    @property
    def get_tall(self):
        return self.tall 

    @tall.setter
    def tall(self, value):
        self.tall=value   



def get_data():
    return 1,2,3

_,a,b = get_data() # 언더라인은 받는 거 무시 하기 

a = [1,2,3]
b = [11,22,33]
mylist = [*a,*b] ##병합 한번씩 쓴다
print(mylist)
c=['a','b']
z=zip(a,c)
print(list(z))

##getter, setter를 정의하는데 decorator 사용


