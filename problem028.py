import math
numLayers=1001/2+1
answer=0
for x in xrange(0,numLayers):
	topRight=math.pow((2*x+1),2)
	twoX=2*x
	answer+=topRight+(math.pow((twoX-1),2)+twoX)+(math.pow(twoX,2)+1)+(topRight-twoX)
print answer-3