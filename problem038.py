largest = 0
for x in xrange(10, 10000):
    counter = 1
    num = ""
    possible = True
    while len(num) <= 9 and possible:
        if len(num) == 9:
            largest = max(largest, int(num))
            counter = 1
            break
        temp = list(str(x * counter))
        counter += 1
        for j in xrange(0, len(temp)):
            if temp[j] in num or temp[j] == '0':
                possible = False
                counter = 1
                break
            else:
                num += temp[j]
print largest
