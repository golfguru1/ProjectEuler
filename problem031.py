coins = [1, 2, 5, 10, 20, 50, 100, 200]
counter = 0
for a in xrange(0, 3):
    for b in xrange(0, 5):
        for c in xrange(0, 11):
            for d in xrange(0, 21):
                for e in xrange(0, 41):
                    for f in xrange(0, 101):
                        for g in xrange(0, 201):
                            if a * 100 + b * 50 + c * 20 + d * 10 + e * 5 + f * 2 + g == 200:
                                counter += 1
print counter + 1
