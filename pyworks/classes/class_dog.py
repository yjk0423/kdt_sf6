class Dog():
    kind = "진돗개" #클래스 변수는 값을 공유하고 유지한다.
    def __init__(self, name):
        self.name = name #인스턴스 변수

dog1 = Dog("나무")
dog2 = Dog("백구")


print(dog1.name)
print(dog2.name)
#사용하지 않음
# print(dog1.kind)
# 클래스 이름.변수 으로 사용한다.
print(Dog.kind)