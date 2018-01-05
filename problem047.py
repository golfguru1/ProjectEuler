def primes(n):
    primfac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n /= d
        d += 1
    if n > 1:
        primfac.append(n)
    return list(set(primfac))


nums = []
for x in xrange(646, 1000000):
    nums.append(x)
for x in xrange(0, len(nums) - 3):
    if len(primes(x)) == len(primes(x + 1)) == len(primes(x + 2)) == len(primes(x + 3)) == 4:
        print x
        break
