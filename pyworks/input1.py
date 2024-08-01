#입략 함수 - input(문자열)
# name = jk

#name = input("이름 입력: ")
#print(f"당신의 이름은 {name} 이군요")


number = int(input("숫자 입력 : "))
print(type(number))

print(int(number) + 1)

num1 = input("1번 수 입력 : ")
num2 = input("2번 수 입력 : ")

print(int(num1) + int(num2))

print(num1 + num2)

#오류 처리(try ~ except 구문)
# :(콜론) - 코드 블럭 ({ })

try:
    num1 = input("1번 수 입력 : ")
    num2 = input("2번 수 입력 : ")

print(int(num1) + int(num2))

except:
    print("정수 입력하시오.")
