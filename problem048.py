def power(x,y):
	answer=1
	for i in xrange(0,y):
		answer*=x
	return answer

answer=0
for x in xrange(1,1001):
	answer+=power(x,x)
print str(answer)[-10:]