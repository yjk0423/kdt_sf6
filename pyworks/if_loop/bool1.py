#비교 연산
# 비교 연산의 결과는 - bool자료(True/False)
b1 = 2 > 1
print(b1) # True

b2 = (2 == 1)
print(b2)

b3 = (2 != 1)
print(b3)

# 논리 연산 - and, or, not
logic1 = (2 > 1) and (2 == 1)
print(logic1)

logic2 = (2 > 1) or (2 == 1)
print(logic2)

logic3 = not(2 != 1)

# 논리 연산 예제
age = 17
under_20 = age < 20

print(under_20)
print(not under_20)
