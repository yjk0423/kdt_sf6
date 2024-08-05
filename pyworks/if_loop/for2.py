#for in list

shop = ["반팔티", "바지", "이어폰", "키보드"]

print("바지" in shop) #True
print("양말" in shop) #False
print("양말" not in shop) #True


shop.append("마우스")

shop.remove("이어폰")

#리스트 요소 추가 (여러개)

shop.extend(["커피", "비스켓"])
print(shop[:])
for i in shop:
    print(i)
    
#리스트의 연산
# 개수, 합계, 평균, 최대값, 최소값
score = [70, 80, 60, 90, 40]
print(f"개수 : {len(score)}")
print(f"합계: {sum(score)}")
print(f"평균: {sum(score) / len(score)}")
print(max(score))
print(min(score))

sum_value = 0
for i in score:
    sum_value += i
print(f"합계: {sum_value}")

#최대값
max_value = 0
for i in score:
    if max_value < i:
        max_value = i
print(max_value)
#최소값
min_value = 10000
for i in score:
    if min_value > i:
        min_value = i
print(min_value)