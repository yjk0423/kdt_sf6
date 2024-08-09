class Calculator:
    def __init__(self):
        self.value = 100

    def sub(self,value):
        self.value -= value
        return self.value

class LimitCalculator(Calculator):

    def sub(self,value):
        if self.value-value > 0:
            super().sub(value)
        else:
            self.value = 0

lc = LimitCalculator()
lc.sub(40)
lc.sub(20)
print(lc.value)