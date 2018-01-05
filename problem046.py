from math import *


def isPrime(n):
    if n == 1:
        return False
    sqroot = int(sqrt(n))
    temp = 2
    while temp <= sqroot:
        if n % temp == 0:
            return False
        temp += 1
    return True


arrayOfPrimes = []
x = 1
while len(arrayOfPrimes) < 10000:
    if isPrime(x):
        arrayOfPrimes.append(x)
    x += 2
found = False
num = 3
while not found:
    if num not in arrayOfPrimes:
        counter = 0
        found = True
        while arrayOfPrimes[counter] < num and counter < len(arrayOfPrimes):
            check = num - arrayOfPrimes[counter]
            if sqrt(check / 2.0) == int(sqrt(check / 2.0)):
                found = False
            counter += 1
    num += 2
print num - 2
