def isPentagonal(x):
	num=0
	counter=0
	while num<x:
		num=nthPentagonal(counter)
		counter+=1
	return num==x

def nthPentagonal(x):
	return x*(3*x-1)/2

def nthTriangle(x):
	return x*(x+1)/2

def isHexagonal(x):
	num=0
	counter=0
	while num<x:
		num=nthHexagonal(counter)
		counter+=1
	return num==x
def nthHexagonal(x):
	return x*(2*x-1)

counter1=166
a=nthPentagonal(counter1)
while not isHexagonal(a):
	counter1+=1
	a=nthPentagonal(counter1)
print a