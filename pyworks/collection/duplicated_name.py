#list, set을 사용 - 중복이름 찾기
name = ["흥부","콩쥐","놀부","콩쥐"]

duplicated_name = set()
n = len(name)

for i in range(0, n-1):
    for j in range(i+1, n):
        if name[i] == name[j]:
            duplicated_name.add(name[i])
"""
    
"""
print(f"중복 이름 : {duplicated_name}")