import random

limit=2
tag = random.randint(1, limit)
print "limit value is " + str(tag)
def gass():
    index = 1
    num = 0
    gassList = {
        'up': limit,
        'down': 0
    }
    while index <= limit :
        if num > tag:
            gassList['up'] = num
            num = dealNum(num, 'big', gassList)
        elif num < tag:
            gassList['down'] = num
            num = dealNum(num, 'small', gassList)
        else:
            print "Your gass %d and you gass value is %d" % (index, num)
            break
        print "index is %d, gass num is %d" %(index, num)
        index += 1

def dealNum(num, tag, gassList):
    result = 0
    if tag == 'big':
        result = (num + gassList['down'])/2
    else:
        result = (num + gassList['up'])/2 + 1
    return int(result)

gass()
