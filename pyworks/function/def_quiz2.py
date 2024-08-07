def get_price(price):
    if price < 20000:
        return price + 2500
    else:
        return price
print(f"상품1 가격: {format(get_price(30000), ",d")}원")
print(f"상품2 가격: {format(get_price(15000), ",d")}원")
