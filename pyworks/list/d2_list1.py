#이차원 리스트 - 리스트 내부에 리스트 있음
# matrix - 행, 열로 이루어짐
d = [
    [10, 20],
    [30,40],
    [50,60]
]

print(d[0][1])
print(d[1][1])
print(d[2][1])

d.append([70,80])
print(d)

#요소 수정
d[0][0] = 90
d[0][1] = 100
print(d)

# 요소 삭제
# d[1].pop(1) # 40 삭제

#리스트의 크기
print("리스트의 크기(행): ", len(d))
print("리스트의 크기(열): ", len(d[0]))

# for i in range(len(d)):
#     for j in range(0, len(d[i])):
#         print(d[i][j], end=" ")
#     print()

# 사용 해도 되나 열 구조가 동일 해야 사용할수 있음
for x, y in d:
    print(x,y)