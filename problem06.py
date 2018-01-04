'''
Created on Apr 15, 2013

@author: markhall
'''

def sumOfSquares(n):
    a=0
    for x in range(1,n+1):
        a+=x*x
    return a
def squareOfSum(n):
    b=0
    for x in range(1,n+1):
        b+=x
    return b*b

print squareOfSum(100)-sumOfSquares(100)