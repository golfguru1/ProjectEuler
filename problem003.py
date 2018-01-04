'''
Created on Apr 15, 2013
 
@author: markhall
'''
def findFactors(n):
    factors=[]
    d=2
    while(n>1):
        while (n%d==0):
            factors.append(n)
            n/=d
        d+=1
    return factors





num=600851475143
greatestDivisor=0
initialFactors=findFactors(num)
for prime in initialFactors:
    if(num%prime==0):
        greatestFactor=prime
print greatestFactor