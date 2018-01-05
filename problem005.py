'''
Created on Apr 15, 2013

@author: markhall
'''


def GCF(num, den):
    while den != 0:
        temp = den
        den = num % den
        num = temp
    return num


def LCM(a, b):
    return (a * b) / GCF(a, b)


def smallestDivisible(start, end):
    solution = 1
    for iterator in range(start, end + 1):
        solution = LCM(solution, iterator)
    return solution


print smallestDivisible(1, 20)
