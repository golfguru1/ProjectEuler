'''
Created on Jul 16, 2013

@author: markhall
'''


def fibonacci(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 3
    else:
        prev = -1
        result = 1
        sum = 0
        for x in xrange(0, n + 1):
            sum = result + prev
            prev = result
            result = sum
        return result


i = 1
while len(str(fibonacci(i))) < 1000:
    i += 1
print i
