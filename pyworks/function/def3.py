# 1부터 n 까지 곱하는 함수
def gob_n(n):
    sumb_v = 1
    for i in range(1,n+1):
        sumb_v *= i
        # print(sumb_v)
    return sumb_v

n = 4
print(gob_n(n))
print(n)