#리스트 함수

#추가 - 리스트.append(), 리스트.insert()
#삭제 - 리스트.pop(), 리스트.remove()
# 정렬 - 리스트.sort() 뒤집기 - reverse()

lower = ["b","c","a","d"]
#
# lower.append("e")
# print(lower)
# lower.pop()
#
# print(lower)
#
# print(len(lower))
#
# # 'b'와 'c' 사이에 'e' 추가
# lower.insert(2, "e")
# print(lower)
#
# lower.remove("e")
# print(lower)

lower.sort() # 아스키코드 기준으로 정렬됨
print(lower)

lower.reverse()
print(lower)
