def simplify(a,b):
	listA=list(a)
	listB=list(b)
	copyA=list(listA)
	copyB=list(listB)
	for x in xrange(0,len(copyA)):
		if copyA[x] in listB:
			listB.remove(copyA[x])
			listA.remove(copyA[x])
			return [listA[0],listB[0]]

numerator=1
denom=1
for x in xrange(10,100):
	for y in xrange(10,100):
		if simplify(str(x),str(y)) is not None:
			a=float(simplify(str(x),str(y))[0])
			b=float(simplify(str(x),str(y))[1])
			if a>0 and b>0:
				if x%10!=0 and y%10!=0 and x%11!=0 and y%11!=0 and x/y<1 and x%y!=0 and a/b==float(x)/float(y):
					print str(x)+"/"+str(y)+" = "+str(int(a))+"/"+str(int(b))
					numerator*=int(a)
					denom*=int(b)
print str(numerator)+"/"+str(denom)