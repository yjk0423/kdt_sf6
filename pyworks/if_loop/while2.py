# while true : 무한 반복 if - break 빠져나옴
from operator import eq

# while True:
#     lunch = input("오늘점심 메뉴: ")
#     print(lunch + "!!")
#
#     if eq(lunch,"그만"):
#         break

# 1 ~ 10 출력
i = 0

while True:
    if i < 10:
        print("ㅎㅇ", end=" ")

    i += 1
    if i == 10:
        break
