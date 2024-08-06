# 실습5
# print(sum([1, 2, 3]))
# print(max([1, 2, 3]))

input_num = input("숫자 입력: ").split(" ")
numbers = []
print(input_num)  # 문자형
a = 0
c = 0
for i in input_num:  # 형변환 과정
    numbers.append(int(i))

print(f"가장큰 값: {max(numbers)}")
print(f"가장작은 값: {min(numbers)}")

a = sum(numbers) - (max(numbers) + min(numbers))
c = len(numbers) - 2
print(f"나머지 값 평균: {a / c}")