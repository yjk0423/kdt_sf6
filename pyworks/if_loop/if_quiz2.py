while True:
    a = int(input("점수를 입력하시오: "))
    succes = ""

    if a < -1:
        print("올바른 점수를 입력해주세요.")
        continue
    if 90 <= a:
        succes = "A"
    elif 80 <= a and a < 90:
        succes = "B"
    elif 70 <= a and a < 80:
        succes = "C"
    elif 60 <= a and a < 70:
        succes = "D"
    elif a < 60:
        succes = "E"
    print(f"{succes} 등급입니다.")
    break

# if a < 0:
#     print("올바른 점수를 입력하시오")
# else:
#     if 90 <= a:
#         succes = "A"
#     elif 80 <= a and a < 90:
#         succes = "B"
#     elif 70 <= a and a < 80:
#         succes = "C"
#     elif 60 <= a and a < 70:
#         succes = "D"
#     elif a < 60:
#         succes = "E"
#     print(f"{succes} 등급입니다.")
