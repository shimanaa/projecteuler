x= 1
for y in range(1,20):
    for z in range(1,20):
        if (x * z) % y == 0:
            x *= z
            break
print(x)
