x = 2000000
out = []
nums = 0
while nums < x:
    prime = True
    nums += 1
    for i in range(2,9):
        if nums % i == 0 and nums != i:
            prime = False
    
    if prime:
        if nums == 1:
            False
        else:
            out.append(nums)

print(sum(out))
