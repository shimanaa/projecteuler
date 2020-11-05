x = 3
y = 5
Max = 1000
outPut = []

while x < Max:
    outPut.append(x)
    x += 3

while y < Max:
    outPut.append(y)
    y += 5

print(sum(outPut))
