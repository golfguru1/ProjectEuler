'''
Created on Jul 17, 2013

@author: markhall
'''
sequenceLength = 0
foundRemainders = [None] * 1000
for i in xrange(1000, 1, -1):
    if sequenceLength >= i:
        break
    value = 1
    position = 0
    while foundRemainders[value] == 0 and value != 0:
        foundRemainders[value] = position
        value *= 10
        value %= i
        position += 1
    if position - foundRemainders[value] > sequenceLength:
        sequenceLength = position - foundRemainders[value]
print sequenceLength
