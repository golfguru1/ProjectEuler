from math import *
import itertools
def isPrime(n):
    sqroot = int(sqrt(n))
    temp = 2
    while temp <= sqroot:
        if n % temp == 0:
            return False
        temp+=1
    return True

for x in xrange(1488,10000):
	if isPrime(x):
		nums=list(set(itertools.permutations(str(x))))
		if len(nums)>=3:
			newArray=[]
			for i in xrange(0,len(nums)):
				if isPrime(float("".join(nums[i]))):
					newArray.append("".join(nums[i]))
		if str(x+3330) in newArray and str(x+6660) in newArray:
			print str(x)+str(x+3330)+str(x+6660)
			break

