sum = 21
while True:
    num = int(input("tage: "))
    if sum == 1:
        print("loose")
        break
    if num >= 5 or num <= 0:
        print("wrong choose")
        continue
    print("Computer took: ", (5-num), sum, "\n")
    sum -= 5
