'''
Created on Apr 15, 2013

@author: markhall
'''
global suM
suM=0
def fibonacci(n):
    global suM
    a=1
    b=1
    c=0
    while(c<n):
        c=a+b
        a=b
        b=c
        if(c%2==0):
            suM+=c

fibonacci(4000000)
print suM
        