# 유용한 문자열 함수
# 개수 - len, 지정한 특정 문자 개수 - count()
# 대문자 변환 - 문자열,upper() 소문자,lower()
# split 문자열을 짤라서 리스트로 변환하는 함수 공식 = 문자열.sprit(구분기호)
f = "바나나"

print(len(f))
print(len("바나나바나나나바나나나바나나나"))

dupl_count = "banana"
print(dupl_count.count("a"))  # count 는 지정한 문자가 몇개가 있는지 알려주는 함수이다.

abc = "hello"
qwe = "HELLO"
print(abc.upper())
print(qwe.lower())

friends = "존 루나 제리"

print(friends.split(" "))

alpha = "a:b:c:d"
print(alpha.split(":"))
alpha.split(":")
print(alpha[0])

# 입력 받아서 리스트 만들기

input_num = input("숫자 입력: ").split(" ")
numbers = []
print(input_num) # 문자형

for i in input_num: # 형변환 과정
    numbers.append(int(i))
print(numbers)
        

email = "condingon@naver.com"
email.split("@")
print(email.split("@"))
print(email[:])

msg = "Hello Python"
print(msg.replace("Python", "C++"))
