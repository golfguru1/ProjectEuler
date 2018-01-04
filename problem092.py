count=0;
for x in xrange(10000000,0,-1):
    digits = [int(l) for l in str(x)]
    found=False
    while not found:
        newNum=0;
        for i in digits:
            newNum+=i*i
        if(newNum==89 or newNum==1):
            if(newNum==89): count+=1
            found=True
        else:
            digits=[int(m) for m in str(newNum)]
print count
