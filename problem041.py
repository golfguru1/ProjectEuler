import itertools
import math


def isPrime(n):
    sqroot = int(math.sqrt(n))
    temp = 2
    while temp <= sqroot:
        if n % temp == 0:
            return False
        temp += 1
    return True


maxNum = 0
for x in xrange(1, 10):
    string = ""
    for y in xrange(1, x + 1):
        string += str(y)
    nums = list(itertools.permutations(list(string)))
    for j in range(0, len(nums)):
        if isPrime(float("".join(nums[j]))) and nums[j] > maxNum:
            maxNum = nums[j]
print "".join(maxNum)
