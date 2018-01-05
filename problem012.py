import time
from math import sqrt


def divisors(n):
    divisors = 0
    for x in xrange(1, int(sqrt(n) + 1)):
        if(n % x == 0):
            divisors += 2
    return divisors


n, i = 1, 2
start = time.time()
while 1 == 1:
    if divisors(n) > 500:
        answer = n
        break
    n += i
    i += 1
end = time.time()

print str(answer) + "\nTook: " + str(int(end - start))
