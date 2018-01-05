def palindrome(x):
    return x == x[::-1]


sum = 0
for x in xrange(0, 1000000):
    if palindrome(str(x)) and palindrome(bin(x)[2:]):
        sum += x

print sum
