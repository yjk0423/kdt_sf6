

class Car:
    model = ""
    cc = 0

    def get_info(self):
        print("모델명 : ", self.model,"베기량", self.cc)

car1 = Car() #인스턴스(객체) = 클래스이름()
print(Car())
print(car1)
car1.model = "아반떼"

print("모델명: ",car1.model)

car1.cc = 1000

print("베기량 : ",car1.cc)

car2 = Car()
car2.model = "BMW"
car2.cc = 2000

car2.get_info()
