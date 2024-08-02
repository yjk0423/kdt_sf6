#문자열은 특별한 1차원 리스트이다.

msg = "Have a nice day!"

print(msg[0])
print(msg[-1])
print(msg[0:4])
print(msg[7:])

#문자열 포맷 서식
# %d -정수, %s - 문자열 %f - 실수

print("나는 %d살입니다." %26)
print("나는 %s살입니다." %"스물여섯")

age = 26
year = 1999

print("나는 %d살입니다." %age)
print("나는 %d살입니다. 그리고 %d년생입니다." %(age,year))

#1인치 - 2.54cm
print("1인치는 %.2fcm 입니다."%2.54)
s = 2.54
print(f"1인치는 {s}cm 입니다.")
unit = 2.54000000
print(f"1인치는 {unit:.2f}cm 입니다.")



#
# 짝수만 나오는것
# for i in range(1,21): # 1부터 21까지의 범위를 두고 반복문 돌리는것 i는 알아서 ++ 된다.
#     if i % 2 == 0:  기존에 알고 있는 for문과 조금 다른 유형
#         print(i);

# 홀수만 나오게 스텝이라는것을 한것이다 1부터 19까지 2씩 증가하는 방법이다.
for i in range(1,21,2):
        print(i);
# str으로 도 가능
for i in range(1, 6, 1):  # 1부터 5까지 1씩 증가
    print('*' * i)

