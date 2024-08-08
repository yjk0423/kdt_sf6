# 가변 매개 변수
# 매개변수의 입력값이 정해지지 않은 변수임
# 변수이름 앞에 '*'를 붙인다.
def calc_avg(*numbers): #[1, 2]
    sum_v = 0
    for i in numbers:
        sum_v += i
    return sum_v / len(numbers)
avg1 = calc_avg(1, 2)
print(avg1)

avg2 = calc_avg(1, 2, 3, 4)
print(avg2)
#반올림 - round(숫자, 자리수)
# -2: 십의자리, -1:일의자리, 0:정수, 1:소수점 첫째, 2:소수점 둘째
round_v1 = round(2.547, 0)
print(round_v1)

round_v2 = round(2.547, 1)
print(round_v2)