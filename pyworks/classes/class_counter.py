class Counter():
    x = 0
    def __init__(self):
        Counter.x += 1


c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.x)

class Counter2:

    def __init__(self):
        self.x = 0
        self.x +=1


c5 = Counter2()
print(c5.x)