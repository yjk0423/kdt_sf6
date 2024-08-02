
my_shop = ["반팔티","청바지","이어폰",["무선키보드","유선키보드"]]

#이어폰을 출력하기
print(my_shop[-1])

my_shop[0] = "긴팔티"
print(my_shop[:])

print(my_shop[-1][1])

#여러개 삭제
del my_shop[0:2] #0번1번 동시에 삭제
print(my_shop[:])


