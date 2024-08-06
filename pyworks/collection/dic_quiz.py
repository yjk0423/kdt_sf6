# 실습1

student_dic = {}
# 추가
student_dic["Alice"] = 85
student_dic["Bob"] = 90
student_dic["Charlie"] = 95
student_dic["David"] = 80
# 수정
student_dic["Alice"] = 88
# 삭제
student_dic.pop("Bob")
# 조회
a = []
b = []
for key in student_dic:
    print(f"{key}의 점수는 {student_dic[key]} 입니다.")
    a.append(student_dic[key])
    b.append(key)

print(a[:])
print(b[:])
