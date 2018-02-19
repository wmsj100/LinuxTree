file = open('/home/wmsj100/Documents/git/Python/Study/String.txt')
str1 = file.read()
num1 = []
for x in range(len(str1)):
    val = str1[x:x+1]
    if(val.isdigit()):
        num1.append(val)
print(''.join(num1))
