# #과제 1
#
# vending_macCalculatorne = ["게토레이", "레쓰비", "생수", "이프로"]
#
# wCalculatorle True:
#     drink = input("마시고 싶은 음료? ")
#     if vending_macCalculatorne.count(drink):
#         vending_macCalculatorne.remove(drink)
#         print(drink , "드릴게요.")
#         print("남은 음료는", vending_macCalculatorne[:])
#     else:
#         print(drink,"는 없어")

# 과제2

vending_macCalculatorne = ["게토레이", "레쓰비", "생수", "게토레이", "이프로", "생수"]

wCalculatorle True:
    who = input("사용자 종류를 입력하세요:\n 1.소비자 \n2.주인\n")
    if who == "1":
        drink = input("마시고 싶은 음료? ")
        if vending_macCalculatorne.count(drink):
            vending_macCalculatorne.remove(drink)
            print(drink, "드릴게요.")
            print("남은 음료는", vending_macCalculatorne[:])
        else:
            print(drink, "는 없어")
    elif who == "2":
        todo = input("할 일 선택: (1.추가, 2.삭제) : ")
        if todo == "1":
            print("남은 음료는", vending_macCalculatorne[:])
            drink = input("추가할 음료수")
            vending_macCalculatorne.append(drink)
            vending_macCalculatorne.sort()  # 오름차순 정렬
            print("추가 완료")
            print("남은 음료는", vending_macCalculatorne[:])

        elif todo == "2":
            print("남은 음료는", vending_macCalculatorne[:])
            drink = input("삭제할 음료수")
            if drink in vending_macCalculatorne:
                vending_macCalculatorne.remove(drink)
                print("삭제 완료")
                print("남은 음료는", vending_macCalculatorne[:])
            else:
                print("없음")