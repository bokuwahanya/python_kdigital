from random import randint

class Die:

    def __init__(self):
        self.sides = []
        for _ in range(6):
            self.sides.append(randint(1,10))
        print("dice: ", self.sides)

    def roll_die(self):
        for _ in range(10):
            selected_side = randint(0,5)
            print("your number :",self.sides[selected_side])
        
My_die = Die()

My_die.roll_die()


# 리스트에 6개의 자리 할당 후 랜덤 숫자 받기



## 딕션너리나 리스트에 6개의 자리를 할당한 다음 랜덤한 숫자를 받아 집어넣는다.
## 여섯개를 개별반복으로 10번 반복한다.
    

## 딕셔녀리나 리스트를 10개나 20으로 늘린다. 