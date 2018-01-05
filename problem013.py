'''
Created on Apr 17, 2013

@author: markhall
'''

f = open("bigassnumbers.txt", 'r')
line = f.readline().strip("\n")
a = 0
while line != "":
    a += int(line)
    line = f.readline().strip("\n")

for x in range(0, 10):
    print str(a)[x],
