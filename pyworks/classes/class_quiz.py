# 실습 1 - 사칙연산 클래스 만들기
import sys


class Hi():

    #생성자 메서드
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        total = self.a+self.b
        return total
    def sub(self):
        total = self.a - self.b
        return total
    def mul(self):
        total = self.a * self.b
        return total
    def div(self):
        if self.b == 0:
            print("0은안됨")
            return sys.exit(0)
        else:
            total = self.a / self.b
            return total

h2 = Hi(10,0)


print(h2.add())
print(h2.sub())
print(h2.mul())
print(h2.div())
