def factorial(n):
	if n==1 or n==0:
		return 1
	else:
		product=1
		while n>1:
			product*=n
			n-=1
		return product
def chose(n,r):
	return factorial(n)/(factorial(r)*factorial(n-r))
counter=0
for x in xrange(1,101):
	for y in xrange(1,x):
		if chose(x,y)>1000000:
			counter+=1
print counter