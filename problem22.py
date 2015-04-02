'''
Created on Apr 18, 2013

@author: markhall
'''
import time
f=open("names.txt",'r')
string=f.read()
a=sorted(string.split(","))
SUM=0
start=time.time()
for x in xrange(1,len(a)+1):
    namesum=0
    for y in xrange(0,len(a[x-1])):
        if(ord(a[x-1][y])!=34):
            namesum+=(ord(a[x-1][y])-64)
    SUM+=(namesum*x)
end=time.time()
print str(SUM)+"\nTook: "+str(end-start)