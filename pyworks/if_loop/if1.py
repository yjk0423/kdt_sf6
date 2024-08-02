# if문 - 조건 : 나이가 15세이상이면 "관람가" 출력


age = 17

if age >= 15:
    print("관람가")

print(f"나이가 {age}입니다.")

if age >= 15:
    print("관람가")
else:
    print("관람이 불가 합니다.")
    print(f"나이가 {age}입니다.")

# 어떤수를 짝수인지 홀수인지 판별하는 프로그램

print("------------------------------------------")
num = int(input("숫자를 입력하세요: "))

if num % 2 == 0:
    print("짝수 입니다.")

elif num % 2 == 1:
    print("홀수 입니다.")

else:
    print("hahaha")
