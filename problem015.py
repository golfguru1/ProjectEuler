'''
Created on Apr 17, 2013

@author: markhall
'''
import time
def getPaths(n):
    return factorial(2*n)/(factorial(n)*factorial(n))

def factorial(n):
    product=1
    while n>0:
        product*=n
        n-=1
    return product
    
start=time.time()

answer=getPaths(20)

end=time.time()

print str(answer)+"\nTook: "+str(int(end-start))