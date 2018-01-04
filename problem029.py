'''
Created on Jul 22, 2013

@author: markhall
'''
array=[]

for x in xrange(2,101):
	for y in xrange(2,101):
		array.append(pow(x,y))
myList=sorted(set(array))
print len(myList) 