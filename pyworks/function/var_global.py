# global - 전역 변수임을 알려주는 키워드, 값을 누적시킬때
# 로직 끝나면 사라짐


def one_up():
    global x
    x += 1
    return x

x = 0

one_up()
one_up()
one_up()
one_up()
print(one_up())
print(x)