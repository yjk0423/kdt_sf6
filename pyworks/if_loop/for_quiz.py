# 실습 1

num = int(input("숫자 입력: "))
total = 0;
total2 = 0;
for i in range(1, num+1):
    total += i
    print(total)

#번외
for i in range(1, num+1):
    if i%2 !=0:
        total2 += i
        print(total2)

#실습2
num2 = int(input("초 입력: "))
total3 = 1;
for i in range(num2, 0, -1):
    print(i, end=" ")
print("발사")