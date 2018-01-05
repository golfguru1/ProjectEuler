import math


def isPrime(n):
    sqroot = int(math.sqrt(math.fabs(n)))
    temp = 2
    while temp <= sqroot:
        if n % temp == 0:
            return False
        temp += 1
    return True


maxA = 0
maxB = 0
maxN = 0
for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        n = 0
        while isPrime(n * n + a * n + b):
            n += 1
        if n > maxN:
            maxA = a
            maxB = b
            maxN = n
print "n^2+(" + str(maxA) + ")n+(" + str(maxB) + ")", maxN
print (maxA * maxB)
