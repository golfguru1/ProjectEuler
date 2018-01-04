def factorial(x):
    factorial=1
    while x>0:
        factorial*=x
        x-=1
    return factorial

answer=0
for x in xrange(3,100000):
	sum=0
	for i in xrange(0,len(str(x))):
		sum+=factorial(int(str(x)[i]))
		if sum==x:
			answer+=x
print answer