#자료구조 - 딕셔너리(dictionary)
# "치킨" : 닭을 튀긴 요리

fruits = {
    "apple": "사과",
    "banana": "바나나",
    "peach": "복숭아"
}
# get()을 이용한 검색
print(fruits.get("apple"))

#요소 추가
fruits["strawberry"] = "딸기"
#요소 수정
fruits["peach"] = "천도복숭아"
#요소 삭제
fruits.pop("banana")
print("--------------------------------------------------")
# 키만 반환
print(fruits.keys())
# 값만 반환
print(fruits.values())
# 키와 값 모두 반환
print(fruits.items())

# 키와 값 전체 조회
for key in fruits.keys():
    print(key, ":", fruits[key])

print(type(fruits))
print(fruits)

# 딕셔너리 생성
dict1 = {1:"a", 2:"b", 3:"c"}
print(dict1)

# key=4, value "추가"

dict1[4] = "d"

print(dict1)