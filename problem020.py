'''
Created on Apr 18, 2013

@author: markhall
'''
import time
def factorial(n):
    product=1
    while n>0:
        product*=n
        n-=1
    return product

a=0
start=time.time()
num=long(factorial(100))
for x in xrange(0,len(str(num))):
    a+=int(str(num)[x])
end=time.time()
print a
print "Took: "
print end-start