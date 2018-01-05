import math


def isPentagonal(x):
    num = 0
    counter = 0
    while num < x:
        num = nthPentagonal(counter)
        counter += 1
    return num == x


def nthPentagonal(x):
    return x * (3 * x - 1) / 2


dif = 0
for i in xrange(1000, 10000):
    for y in xrange(1000, 10000):
        a = nthPentagonal(i)
        b = nthPentagonal(y)
        if isPentagonal(math.fabs(b - a)) and isPentagonal(b + a) and b != a:
            print i, y
            dif = math.fabs(b - a)
            break
    else:
        continue
    break
print dif
