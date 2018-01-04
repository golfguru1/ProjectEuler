import math
answer=0
for x in xrange(2,1000000):
	check=0
	for i in xrange(0,len(str(x))):
		check+=math.pow(float(str(x)[i]),5)
	if check==x:
		answer+=x
print answer