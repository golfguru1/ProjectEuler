import itertools
import math
def isPrime(n):
	if n==1:
		return False
	sqroot = int(math.sqrt(math.fabs(n)))
	temp=2
	while temp <= sqroot:
		if n % temp == 0:
			return False
		temp+=1
	return True

counter=0
for i in xrange(1,1000000,2):
	if isPrime(i):
		numArray=list(str(i))
		areTheyPrime=[]
		for x in xrange(0,len(str(i))):
			string=""
			for m in xrange(0,len(numArray)):
				string+=numArray[m]
			areTheyPrime.append(isPrime(float(string)))
			numArray.append(numArray.pop(0))
		if False not in areTheyPrime:
			counter+=1
print counter+1