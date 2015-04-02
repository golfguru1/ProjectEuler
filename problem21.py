'''
Created on Apr 18, 2013

@author: markhall
'''
import time
def d(n):
    a=0
    for x in xrange(1,n):
        if(n%x==0):
            a+=x
    return a          

b=0
start=time.time()
for x in xrange(1,10000):
    sum1=d(x)
    if(sum1!=x):
        sum2=d(d(x))
        if(sum2==x):
            b+=x
end=time.time()
print b
print "Took:"
print end-start