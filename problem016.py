'''
Created on Apr 17, 2013

@author: markhall
'''
import time
start = time.time()
num = long(pow(2, 1000))
a = 0
for x in xrange(0, len(str(num))):
    a += int(str(num)[x])
end = time.time()
print str(a) + "\nTook: " + str(int(end - start))
