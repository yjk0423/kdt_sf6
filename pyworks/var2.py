"""
변수 선언(변수명 만드는 문법)
숫자로 시작하면 안됨
공백이 있으면 안됨
특수문자 안됨 가능한것들 모음(_, )


에러

1. 실행전 에러(컴파 일러)
2. 실행후 에러(런타임 에러)

"""

seson = "여름"

print(seson)

name = "a"
name = "b"

print(name)

print("***회원가입***")
user_id = "qwer"
user_pw = "ser123"
email = "jerry@korea.com"


#print("아이디: " + user_id)
print(f"아이디 : {user_id}")
print("비밀번호: " + user_pw)

#소수점 처리하기
n1 = 10
n2 = 3
div = n1 / n2

print(f'결과값: {div : .1f}')
print(f'결과값: {round(div, 2)}')
# 반올림 함수 - round(숫자, 자리수)
print(round(1.647, 2))
