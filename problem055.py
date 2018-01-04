answerNum=0
answer=0
outside=0
for y in xrange(1,10000):
	found=False
	x=y
	for j in xrange(0,50):
		answer=x+int(str(x)[::-1])
		x=answer
		if str(answer)==str(answer)[::-1]:
			found=True
			break
	if not found:
		answerNum+=1
print answerNum