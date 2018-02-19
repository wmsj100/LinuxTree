basic = 1500
paste = 200
lilv = 0.02
count = int(input("Enter count: "))
price = int(input("Enter price: "))
money = basic + count*(price * lilv + 200)
print("moneyey : {:.2f}".format(money))
