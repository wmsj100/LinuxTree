while True:
    n = int(input("Enter a int: "))
    if n < 0:
        continue
    elif n == 0:
        break
    print("Square is ", n**2)
print("GoodBye")
