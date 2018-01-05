'''
Created on Apr 17, 2013

@author: markhall
'''
import time
start = time.time()
a = []
f = open("numtriangle.txt", 'r')
line = f.readline()
counter = 0
while line != "":
    a.append(line.strip("\n").split(" "))
    line = f.readline()
for m in xrange(0, len(a)):
    for n in xrange(0, len(a[m])):
        a[m][n] = int(a[m][n])
for x in xrange(len(a) - 2, -1, -1):
    for y in xrange(0, len(a[x])):
        if a[x + 1][y] > a[x + 1][y + 1]:
            a[x][y] += a[x + 1][y]
        else:
            a[x][y] += a[x + 1][y + 1]
end = time.time()

print str(a[0][0]) + "\nTook: " + str(int(end - start))
