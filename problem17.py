'''
Created on Apr 17, 2013

@author: markhall
'''
num1to9 = 36
num10 = 3
num11to19 = 67
num20to99 = 10*(6+6+5+5+5+7+6+6) + 8*num1to9
num1to99 = num1to9 + num10 + num11to19 + num20to99
numofsingledigits = num1to9*100
numofdoubledigits = num1to99*9
numofhundred = 7*9
numofhundredand = 9*99*10
num100to999 = numofsingledigits + numofdoubledigits + numofhundred + numofhundredand
total = num1to99 + num100to999 + 11
print total