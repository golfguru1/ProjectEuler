from operator import *
import re
f=open("cipher1.txt",'r')
string=f.read()
a=string.strip("\n").split(",")
counter=100
string=""
for x in xrange(0,len(a)):
	string+=chr(int(a[x]))
while re.match('^[A-Za-z \t]+$',string) is None and counter<1000:
	string=""
	for x in xrange(0,len(a)):
		num=xor(int(a[x]),counter)
		string+=chr(num)
	# print string
	counter+=1
print string
# for x in xrange(0,len(b)):
# 	print chr(b[x]),