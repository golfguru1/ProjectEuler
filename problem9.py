'''
Created on Apr 16, 2013

@author: markhall
'''
import time

start=time.time()
for c in range(1000):
    for b in range(c):
        for a in range (b):
            if(a*a+b*b==c*c and a+b+c==1000):
                print a*b*c
                break
end=time.time()

print "\nTook: "+str(int(end-start))