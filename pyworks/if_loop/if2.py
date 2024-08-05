from operator import eq
#다중 조건문
# 연령이 20대인 경우 성별이 여이면 "20대 여성입니다."
age = int(input("나이를 입력하시오: "))
gender = input("남 or 여 으로 입력하시오: ")
if age >= 0 and age < 20:
    print("미성년자 입니다.")

elif age >= 20 and age < 30:
    if eq(gender, "남"):
        gender = "남성"
    else :
        gender = "여성"
elif age >= 30 and age < 40:
    if eq(gender, "남"):
        gender = "남성"
    else:
        gender = "여성"
else:
    print("중년 입니다.")

print(f"{age}대 {gender} 입니다.")