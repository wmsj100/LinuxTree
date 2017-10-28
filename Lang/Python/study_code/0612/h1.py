import random, time
from random import *
from time import *

date1 = (2008, 1, 1, 0, 0,0,-1, -1, -1)
date2 = (2009, 1, 1, 0, 0,0,-1, -1, -1)

time1 = mktime(date1)
time2 = mktime(date2)

random_time = uniform(time1, time2)

a = input('num: ')
sum = 0
for i in range(int(a)):
    sum += randrange(6) + 1
print 'result is : ' + str(sum)

