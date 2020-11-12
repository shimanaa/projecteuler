PrimeNums = []
Target = 10001
Number = 0
while len(PrimeNums) < Target:
    isPrime = True
    Number += 1
    for x in range(2,9):
        if Number % x == 0 and Number != x:
            isPrime = False
    if isPrime:
        if Number == 1:
            False
        else:
            PrimeNums.append(Number)


print(PrimeNums[-1])
