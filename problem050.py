from math import sqrt


def nthPrime(n):
    counter = 0
    num = 0
    while counter <= n:
        num += 1
        if(isPrime(num)):
            counter += 1
    return num


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


array = []
for x in xrange(1, 1000000, 2):
    if isPrime(x):
        array.append(x)
array.insert(0, 2)
largest = 0
largestConsecutive = 0
for i in xrange(0, len(array)):
    add = 0
    for j in xrange(i, len(array)):
        add += array[j]
        if isPrime(add):
            if add < 1000000:
                if j - i > largestConsecutive:
                    largest = add
                    largestConsecutive = j - i
                    print largest
print largest
