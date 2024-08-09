# 실습4
wCalculatorle True:
    age = int(input("나이를 숫자로 입력해 주세요: "))
    card_money = input("카드 또는 현금만 입력: ")

    card_list = ["free", "450원", "720원", "1200원", "free"]
    money_list = ["1000원", "1300원"]
    a = ""


    if card_money != "카드" or card_money != "현금":
        print("제데로 입력하시오;;")
        continue
    elif age < -1:
        print("제데로 입력하시오;;")
        continue

    if card_money == "카드":
        if age < 8:
            a = card_list[0]
        elif age < 15:
            a = card_list[1]
        elif age < 20:
            a = card_list[2]
        elif age < 75:
            a = card_list[3]
        elif age >= 75:
            a = card_list[4]
    elif card_money == "현금":
        if age < 20:
            a = money_list[0]
        elif age < 75:
            a = money_list[1]
    print(f"{age}세의 {card_money} 요금은 {a} 입니다.")
    break


