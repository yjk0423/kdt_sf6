# 생성자 def __init__()

class Car:
    def __init__(self,model,year):
        self.model = model
        self.year = year

    def show_info(self):
        print(f"모델명: {self.model}, 연식: {self.year}")

# car_a = Car("아이오닉6",2021)
# car_a.show_info()
#
# Car("스포티지",2020).show_info()

cars = [
    Car("쏘나타",2020),
    Car("K5",2017),
    Car("모닝",2022)
]
cars[0].show_info()

print("*Car_List*")
for i in cars:
    i.show_info()

