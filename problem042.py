def isTriangleNum(x):
    counter = 0
    num = 1
    while num < x:
        num = 0.5 * counter * (counter + 1)
        counter += 1
    return num == x


f = open("words.txt", 'r')
string = f.read()
string = string.replace('"', "")
a = sorted(string.split(","))
answer = 0
for x in xrange(0, len(a)):
    numToCheck = 0
    for y in xrange(0, len(a[x])):
        numToCheck += ord(a[x][y]) - 64
    if isTriangleNum(numToCheck):
        answer += 1
print answer
