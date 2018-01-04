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
def lTr(n):
	primes=[]
	while len(str(n))>0:
		primes.append(isPrime(int(n)))
		n=str(n)[1:]
	return False not in primes
def rTl(n):
	primes=[]
	while len(str(n))>0:
		primes.append(isPrime(int(n)))
		n=str(n)[:-1]
	return False not in primes

counter=0
num=11
answer=0
while counter<11:
	if lTr(num) and rTl(num) and isPrime(num):
		answer+=num
		counter+=1
	num+=2
print answer