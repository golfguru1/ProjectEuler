answer = 0
num = [3, 7]
denom = [2, 5]
for x in xrange(2, 1001):
    num.append(num[x - 1] * 2 + num[x - 2])
    denom.append(denom[x - 1] * 2 + denom[x - 2])
for x in xrange(0, len(num)):
    if len(str(num[x])) > len(str(denom[x])):
        answer += 1
print answer
