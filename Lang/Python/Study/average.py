N = 5
count = 0
sum = 0
while count < N:
    sum = sum + float(input("Enter the {} number: ".format(count+1)))
    count = count + 1
average = sum / N
print("N={}, Sum = {}".format(N, sum))
print("the average is {:.2f}".format(average))
