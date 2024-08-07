# 학생 5명의 국어, 수학 총점과 평균

score = [
    [80, 70],
    [70, 95],
    [60, 90],
    [50, 75],
    [75, 60]
]

# 개인별 총점 과 평균
students = []
total = 0
for i in range(len(score)):
    total = score[i][0] + score[i][1]
    students.append(total)
    print(total, total / 2)

print(students)
# 과목별 총점과 평균
sum_subject = [0,0]
avg_subject = [0.0,0.0]
for i in range(len(score)):
    sum_subject[0] += score[i][0]
    sum_subject[1] += score[i][1]

print("국어 총점 : ",sum_subject[0])
print("국어 평균 : ",sum_subject[0] / len(score))
print("수학 총점 : ",sum_subject[1])
print("수학 평균 : ",sum_subject[1] / len(score))
