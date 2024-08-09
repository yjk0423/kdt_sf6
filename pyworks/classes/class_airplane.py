class Airplane:
    # __init__() 생략해도 상관없음
    # def __init__(self):
    #     print("비행기 클래스")

    def take_off(self):
        print("이륙")

    def fly(self):
        print("일반 비행")
    def land(self):
        print("착륙")

class SuperSonicAirplane(Airplane):
# 비행모드 1 - NORMAL, 2- SUPERSONIC
    NORMAL = 1 # 클래스 상수
    SUPERSONIC = 2

    def __init__(self):
        self.fly_mode = SuperSonicAirplane.SUPERSONIC

    def fly(self):
        if self.fly_mode == SuperSonicAirplane.SUPERSONIC:
            print("비행기가 초음속 비행합니다.")
        else:
            super().fly()


sa = SuperSonicAirplane()
sa.take_off()
sa.fly()
sa.fly_mode = SuperSonicAirplane.NORMAL
sa.fly()
sa.land()
