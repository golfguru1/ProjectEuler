f = open("keylog.txt", 'r')
line = f.readline().strip("\n")
a = []

while line != "":
    a.append(line)
    line = f.readline().strip("\n")

print a
