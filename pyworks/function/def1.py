def hello():
    print("qwe")    #지역 영역
    return 1
def greeting(name):
    print(name)

def gugudan(dan):
    for i in range(1,10):
        print(f"{dan} x {i} = {dan * i}")

def add(x, y):
    total = x + y
    print(total)
def square(x):
    return x * x
def myabs(x):
    if x < 0:
        return -x
    else:
        return x

def mul(x,y):
    return x * y


# 메인 영역
asw = hello()
greeting("fuck")
print(asw)
gugudan(2)
add(2,1)
a = 5
print(square(a))
print(a)
# 절대값 구하는 함수 - abs(x)
# print(abs(-10)) # abs(): 10 출력 (양수가 무족건나옴)
print(myabs(-2323))
print(mul(5,2))
