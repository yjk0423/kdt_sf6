# 튜플(tuple) - 소괄호, 읽기 전용(수정, 삭제 안됨)

t1 = (10, 20, 30)

print(t1)
print(type(t1))
# 요소 접근 - 읽기(검색)
# print(t1[-1])

# 튜플은 수정이 안됨
# 삭제도 안됨
# t1[1] = 55
# del t1[2]

print(t1[:])

t2 = (7)
print(t2)
print(type(t2))

# 여소를 1개 생성할때 쉼표를 넣어줌
t3 = (7,)
print(t3)
print(type(t3))

# 튜플 요소의 합
print(sum((10, 20 ,30)))
# 튜플 요소의 max
print(min((10, 20 ,30)))
# 튜플 요소의 min
print(max((10, 20 ,30)))

tu1 = (1,2,3)
tu2 = (4,)
tu3 = tu1+tu2
print(tu3)
print(tu3[:])


