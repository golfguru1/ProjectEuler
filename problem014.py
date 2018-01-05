'''
Created on Apr 17, 2013

@author: markhall
'''
import time


def collatz(n):
    counter = 0
    while(n > 1):
        if(n % 2 == 0):
            n /= 2
            counter += 1
        else:
            n = n * 3 + 1
            counter += 1
    return counter + 1


maxChain = 0
start = time.time()
for x in xrange(0, 1000000):
    a = collatz(x)
    if(a > maxChain):
        maxChain = a
        answer = x
end = time.time()

print str(answer) + "\nTook: " + str(int(end - start))
