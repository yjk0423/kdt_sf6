#for i range(시작값, 종료값, 증감값):
# for i in 리스트

a = range(10)
b = range(1,11) # 끝값은 -1 이다
c = range(1,11,2) # 마지막은 증감값

print(list(a)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(b)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(c)) # [1, 3, 5, 7, 9]

# for 1~10 더하기
total = 0
for i in range(1, 11):
    #print(i, end=" ")

    total += i
    print(total, end=" ")

print(total)