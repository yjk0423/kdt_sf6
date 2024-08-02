#실습1
name = input("이름을 입력하시오: ")
age = int(input("나이를 입력하시오: "))

print(f"안녕하세요!"+name+f"님 ({age}세)")

#실습2
try:
    name2 = input("이름을 입력하시오: ")
    birth_year = int(input("태어난 년도를 입력하세요.: "))
    year = int(input("올해 년도를 입력하세요.: "))

    succes = year - birth_year

    print(f"올해는{year}년,{name2}님의 나이는{succes}세 입니다")

except ValueError:
    print("정수로 입력해주세요.")
