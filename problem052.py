found = False
counter = 1
answer = 0
while not found:
    twice = counter * 2
    three = counter * 3
    four = counter * 4
    five = counter * 5
    six = counter * 6
    if sorted(list(str(counter))) == sorted(list(str(twice))) == sorted(list(str(three))) == sorted(list(str(four))) == sorted(list(str(five))) == sorted(list(str(six))):
        found = True
        answer = counter
    counter += 1
print answer
