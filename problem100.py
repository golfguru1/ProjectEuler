'''
Created on Apr 17, 2013

@author: markhall
'''
from math import sqrt
c = float((1 + sqrt(1 + 4*5*pow(10, 23)))/2)
i = 1
while c!=int(c):
    c1 = 0.5*((pow(10,12)+i)*(pow(10,12)+i)-(pow(10,12)+i-1))
    c = float((1 + sqrt(1 + 4*c1)/2))
    i+=1
    print long(c)