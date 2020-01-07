import random

limit=10000
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

def gass1(lower=0, upper=limit, index=0):
    'use digui'
    index +=1
    if lower == upper:
        upper -= 1
        print "gass %d count value is %d" % (index, upper)
        return upper
    else:
        middle = (lower + upper) // 2
        if middle > tag:
            return gass1(lower, middle, index)
        else:
             return gass1(middle+1, upper, index)


gass() # Your gass 12 and you gass value is 9431
gass1() # gass 15 count value is 9431
