import math


def isPrime(n):
    sqroot = int(math.sqrt(n))
    temp = 2
    while temp <= sqroot:
        if n % temp == 0:
            return False
        temp += 1
    return True


sideLength = 2
found = False
primes = 0
notPrimes = 0
while not found:
    array = []
    x = math.ceil(sideLength / 2)
    twoX = 2 * x
    topRight = math.pow((twoX + 1), 2)
    topLeft = math.pow((twoX - 1), 2) + twoX
    bottomLeft = math.pow(twoX, 2) + 1
    bottomRight = topRight - twoX
    array.append(topRight)
    array.append(topLeft)
    array.append(bottomLeft)
    array.append(bottomRight)
    for y in xrange(0, len(array)):
        if isPrime(array[y]):
            primes += 1
        else:
            notPrimes += 1
    # print primes
    if primes / float(primes + notPrimes + 1) < 0.1:
        found = True
    sideLength += 2
print sideLength - 1
