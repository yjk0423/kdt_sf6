# 정보 은닉(보안을 유지하기 위해 접근을 허용하지 않음)
# 접근 제어자 - public(기본), private, protected
# 외부로 쓰지 않고 내부적으로 작동함

class Person():
    # 언더 스코어(__) 2개를 쓰면 접근할 수 없음
    def __init__(self):
        self.__name = ""
        self.__age = 0

    # get set 매서드를 만들어서 접근
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def set_age(self):
        return self.__age


p1 = Person()
p1.name = "as"
print(p1.name)
