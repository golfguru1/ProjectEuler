'''
Created on Apr 15, 2013

@author: markhall
'''


def palindrome(x):
    if x == int(str(x)[::-1]):
        return True


largePalindrome = 0
for x in range(100, 999):
    for y in range(100, 999):
        if palindrome(x * y) and x * y > largePalindrome:
            largePalindrome = x * y
print largePalindrome
