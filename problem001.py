'''
Created on Apr 15, 2013

@author: markhall
'''
a = 0
for x in range(0, 1000):
    if x % 3 == 0 or x % 5 == 0:
        a += x
print a
