class Calculator:
    def __init__(self):
        self.x = 0 #인스턴스 변수

    def add(self, y):
        a = self.x + y
        self.x = self.sub(a)  # sub 메서드의 결과를 self.x에 저장
        return self.x

    def sub(self, z):
        z -= 5
        return z

c1 = Calculator()
print(c1.x)            # 초기값 0 출력
print(c1.add(10))       # add 메서드 실행 후 결과 출력
print(Calculator().add(10))