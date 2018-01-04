'''
Created on Apr 15, 2013

@author: markhall
'''
from math import sqrt
def nthPrime(n):
    counter=0
    num=0
    while counter<=n:
        num+=1
        if(isPrime(num)):
            counter+=1
    return num

def isPrime(n):
    sqroot = int(sqrt(n))
    temp = 2
    while temp <= sqroot:
        if n % temp == 0:
            return False
        temp+=1
    return True
 
print nthPrime(10001)