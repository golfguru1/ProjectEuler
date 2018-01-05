def power(x, y):
    answer = 1
    for i in xrange(0, y):
        answer *= x
    return answer


answer = 0
for a in xrange(1, 100):
    for b in xrange(1, 100):
        add = 0
        powerNum = power(a, b)
        powerNum = str(powerNum)
        for x in xrange(0, len(powerNum)):
            add += int(powerNum[x])
        answer = max(answer, add)
print answer
