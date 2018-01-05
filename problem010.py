'''
Created on Apr 16, 2013

@author: markhall
'''
num = 2000000
array = [True] * (num)
for x in range(2, num + 1):
    multi = 2
    while x * multi <= (len(array) - 1):
        array[x * multi] = False
        multi += 1

a = 0
for x in range(len(array)):
    if array[x]:
        a += x

print a - 1
