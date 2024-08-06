# 자료구조 - set -{}
# 중복이 안됨, 순서가 없다(인덱싱 안됨)

# cart = {"양파", "쌀","콩나물", "쌀", "양파"}
# print(cart)

cart = {"양파", "쌀","콩나물", "쌀"}
print(cart)

# 빈 집합 생성 - set
s1 = set()

s1.add("a")
s1.add("b")
s1.add("c")

s1.remove("c")
print(s1)
# s1.clear()
print(s1)

print("a" in s1)
print("b" in s1)

a = [1, 1, 1 ,2 ,3 ,4 ,5]

print(set(a)) # 셋으로 리스트 중복 제거
print(list(set(a))) # 다시 리스트으로



