#다중 조건문

age = 25

if age < 20:
    print("미성년자 입니다.")

elif age < 30:
    print("20대 입니다.")
elif age < 40:
    print("청년 입니다.")
elif age < 50:
    print("중년 입니다.")
else:
    print("할아버지 입니다.")

print(f"나이는 {age}입니다.")