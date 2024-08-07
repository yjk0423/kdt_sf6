a = [1,2,3,4]

total = 0
for i in a:
    total += i

# 2차원 리스트의 합계와 평균
d = [
        [1],
        [2,3],
        [4,5,6],
     ]
sum_v = 0
count = 0
for i in range(len(d)):
    for j in range(len(d[i])):
        sum_v += d[i][j]
        count += 1
print("합 : ",sum_v)
print("평균 : ", sum_v / count)

print(count)