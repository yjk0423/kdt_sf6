#인스턴수 변수와 클래스 변수

class Dog:
    tricks = []
    def __init__(self, name):
        self.name = name

    def add_trick(self,trick):
        self.tricks.append(trick)

dog1 = Dog("존")

dog1.add_trick("몸 뒤집기")
print(Dog.tricks)
dog2 = Dog("제리")
dog2.add_trick("죽은척 하기")
print(Dog.tricks)



