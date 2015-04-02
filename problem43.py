import itertools
nums=list(itertools.permutations("0123456789"))
answer=0
array=[2,3,5,7,11,13,17]
for j in xrange(0,len(nums)):
	numString="".join(nums[j])
	primes=[]
	for i in xrange(1,len(numString)-2):
		if int(numString[i:i+3])%array[i-1]==0:
			primes.append(True)
		else:
			primes.append(False)
	if False not in primes:
		answer+=int(numString)
print answer
