def get_price():
    price = 4000 * quantitiy
    return price


def one_up():
    x = 0
    x += 1
    return x

print(one_up())

quantitiy = 2
order_price = get_price()
print(f"{quantitiy}게에 {order_price}원 입니다.")
