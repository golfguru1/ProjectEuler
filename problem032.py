answer=0
a=[]
for i in xrange(100,1000):
	for j in xrange(10,100):
		product=i*j
		num=str(product)+str(i)+str(j)	
		if len(num)==9 and str(1) in num and str(2) in num and str(3) in num and str(4) in num and str(5) in num and str(6) in num and str(7) in num and str(8) in num and str(9) in num:
			if product not in a:
				a.append(product)		
				print str(i)+"*"+str(j)+"="+str(product)
				answer+=product
for i in xrange(2,10):
	for j in xrange(1000,10000/i):
		product=i*j
		num=str(product)+str(i)+str(j)	
		if len(num)==9 and str(1) in num and str(2) in num and str(3) in num and str(4) in num and str(5) in num and str(6) in num and str(7) in num and str(8) in num and str(9) in num:
			if product not in a:
				a.append(product)		
				print str(i)+"*"+str(j)+"="+str(product)
				answer+=product
print answer

