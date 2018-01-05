string = ""
counter = 1
while len(string) < 1000000:
    string += str(counter)
    counter += 1
stringList = list(string)
answer = int(stringList[0]) * int(stringList[9]) * int(stringList[99]) * int(
    stringList[999]) * int(stringList[9999]) * int(stringList[99999]) * int(stringList[999999])
print answer
