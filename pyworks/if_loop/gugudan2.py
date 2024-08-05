#
# #구구단 2 ~ 9 단까지
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{i} x {j} = {i * j}")


for i in range(1, 5):
    for j in range(1, 5):
        print("가", end=" ")
    print() #행바꿈


for i in range(1, 5):
    for j in range(1, i + 1):
        print("*", end=" ")
    print() #행바꿈

# * 찍기 하나씩 늘어나게
star = "*"
a = " "
# for i in range(1, 5):
#     print(star * i)

# for i in range(4, 0, -1):
#     print(star * i)

for i in range(1,5):
    for j in range (1, 6 - i):
        print("*", end=" ")
    print()

for i in range(1, 5):
    print(star * i)
print("------------------------------")
for i in range(1, 5):
    print(star * (5 -i))
print("------------------------------")
for i in range(1, 5):
    print(" " * (4-i) + "*" * i)

#숫자가 연속으로 증가하는 알고리즘
for i in range(0,4):
    for j in range(1,5):
        if i * 4 + j > 15:
            break
        print(i * 4 + j, end=" ")
    print()