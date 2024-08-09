# 모듈(modul) 불러오기
from classes.class_quiz import Calculator
import sys

# print(cal.add())
# print(cal.sub())
# print(cal.mul())
# print(cal.div())

# Calculator 상속 받기

class MoreCalculator(Calculator):
    # 거듭 제곱 계산 기능 추가
    def pow(self):
        return self.a ** self.b
    def divide(self):
        try:
            return self.a / self.b
        except:
            print("0")
    def div(self):
        try:
            super().div()
        except:
            print()

mc = MoreCalculator(6,4)
print(mc.add())
print(mc.pow())
print(mc.mul())
print(mc.div())
