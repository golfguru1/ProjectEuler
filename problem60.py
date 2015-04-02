import itertools
from math import *
from random import *
def isPrime(n):
	if n==1:
		return False
	sqroot=int(sqrt(n))
	temp=2
	while temp <= sqroot:
		if n % temp == 0:
			return False
		temp+=1
	return True

x=[]
for i in xrange(1,100000,2):
	if isPrime(i):
		x.append(i)
x.insert(0,2)
done=False
# while not done:
boolArray=[]
answer=[]
for i in xrange(0,len(x)):
	for j in xrange(i+1,len(x)):
		nums=list(set(itertools.permutations([str(x[i]),str(x[j])],2)))
		for i in xrange(0,len(nums)):
			boolArray.append(isPrime(int("".join(nums[i]))))
		if False not in boolArray:
			# done=True
			answer.append([int("".join(nums[0])),int("".join(nums[1]))])
print answer





