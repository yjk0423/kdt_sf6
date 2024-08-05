#과제 1

vending_machine = ["게토레이", "레쓰비", "생수", "이프로"]

while True:
    dirnk = input("마시고 싶은 음료? ")
    if vending_machine.count(dirnk):
        vending_machine.remove(dirnk)
        print(dirnk , "드릴게요.")
        print("남은 음료는", vending_machine[:])
    else:
        print(dirnk,"는 없어")

