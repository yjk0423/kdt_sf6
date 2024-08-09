class Health:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100

    def getname(self):
        return self.__name

    def sethp(self, hp):
        if hp < 0:
            hp = 0
        if hp > 100:
            hp = 100
        self.__hp = hp

    def gethp(self):
        return "hp: " + str(self.__hp)

    def exercise(self, hours):
        self.sethp(self.__hp + hours)
        print("{}시간 운동하다".format(hours))
        
    def drink(self, coups):
        self.sethp(self.__hp - coups)
        print("술을 {}잔 마시다".format(coups))

h1 = Health("jay")
h1.sethp(5)
h1.exercise(1)
print(f"{h1.getname()} - {h1.gethp()}")