import math
array = [0] * 1000
for a in xrange(1, 1000):
    for b in xrange(1, 1000 - a):
        c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
        if a + b + c <= 1000 and c % int(c) == 0.0:
            array[a + b + int(c) - 1] += 1
maxNum = 0
maxIndex = 0
for i in xrange(len(array)):
    if array[i] > maxNum:
        maxNum = array[i]
        maxIndex = i
print maxIndex + 1
print maxNum
