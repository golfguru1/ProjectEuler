nums = [1] + [0] * 100
nums[0] = 1

for i in xrange(1, 100):
    for j in xrange(i, 101):
        nums[j] += nums[j - i]

print nums[-1]
