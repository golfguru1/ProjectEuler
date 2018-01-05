'''
Created on Apr 18, 2013

@author: markhall
'''


def sumOfFactors(n):
    sum = 0
    for divisor in range(1, n):
        if(n % divisor == 0):
            sum += divisor
    if(sum > n):
        return True
    else:
        return False


arrayOfAbundants = []
for x in xrange(2, 28123):
    if(sumOfFactors(x)):
        arrayOfAbundants.append(x)

array = [False] * 28124
for i in xrange(0, len(arrayOfAbundants)):
    for y in xrange(i, len(arrayOfAbundants)):
        if(arrayOfAbundants[i] + arrayOfAbundants[y] <= 28123):
            array[arrayOfAbundants[i] + arrayOfAbundants[y]] = True
        else:
            break
answerSum = 0
for m in xrange(0, 28123):
    if array[m] == False:
        answerSum += m
print answerSum
