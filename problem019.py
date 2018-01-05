'''
Created on Apr 17, 2013

@author: markhall
'''
import time


def leapYear(year):
    if (year % 400 == 0):
        return True
    elif(year % 100 == 0):
        return False
    elif(year % 4 == 0):
        return True
    else:
        return False


a = 0
start = 3
startT = time.time()
for x in xrange(1901, 2001):
    for month in xrange(1, 13):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            start += 3
        elif month == 2:
            if(leapYear(x)):
                start += 1
        else:
            start += 2
        if start % 7 == 0:
            a += 1
end = time.time()

print (a)
print "Took: "
print end - startT
