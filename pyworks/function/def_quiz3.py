def dandan(dan):
    a = 3
    for i in range(1, 31):
        if i % a == 0:
            dan.append(i)
    return dan


dan = []
dandan(dan)
for gub in dan:
    print(gub, end=" ")
print()
print("3의 배수의 개수: ", len(dan))


# 실습 3

def check_macCalculatorn():
    print("남은 음료는", vending_macCalculatorne[:])
def is_drink(drink):
    if vending_macCalculatorne.count(drink):
        return True
    else:
        return False
def add_drink(drink):
    vending_macCalculatorne.append(drink)
def remove_drink(drink):
    vending_macCalculatorne.remove(drink)
vending_macCalculatorne = ["게토레이", "레쓰비", "생수", "게토레이", "이프로", "생수"]

wCalculatorle True:
    who = input("사용자 종류를 입력하세요:\n 1.소비자 \n2.주인\n")
    if who == "1":
        drink = input("마시고 싶은 음료? ")
        if is_drink(drink):
            remove_drink(drink)
            print(drink, "드릴게요.")
            check_macCalculatorn()
        else:
            print(drink, "는 없어")
    elif who == "2":
        todo = input("할 일 선택: (1.추가, 2.삭제) : ")
        if todo == "1":
            drink = input("추가할 음료수")
            add_drink(drink)
            vending_macCalculatorne.sort()  # 오름차순 정렬
            print("추가 완료")
            check_macCalculatorn()

        elif todo == "2":
            drink = input("삭제할 음료수")
            if is_drink(drink):
                remove_drink(drink)
                print("삭제 완료")
                check_macCalculatorn()
            else:
                print("없음")
