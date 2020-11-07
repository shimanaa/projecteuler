x = 600851475143
output = []

for i in range(2, x):
    Calc = x % i
    if Calc == 0:
        output.append(i)


result = []
for y in output:
    primeNum = True
    for test in range(2, y):
        if (y % test  == 0):
            primeNum = False
    if primeNum:
        result.append(y)
        for largNUm in result:
            if largNUm > result[0]:
                result[0] = largNUm
            
print(result[0])