score = [10,20,30,40,80]
#인덱싱: 특정한 한 개 요소에 접근
print(score[2])

# 슬라이싱: 여러개 요소에 접근
print(score[0:3]) #처음부터 2번까지 접근
print(score[:3])
print(score[3:]) # 3부터 끝까지 접근
print(score[:]) # 전 요소 출력 or 접근

#요소 수정
score[1] = 50
#요소 삭제
del score[2]

for i in range(1, 6):
    print('*' * i)