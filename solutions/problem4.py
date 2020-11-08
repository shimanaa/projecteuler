output = []
outputX = []
outputY = []
end = []
i = 0
for x in range(0,1000):
    for y in range(0,1000):
        outputX.append(x)
        outputY.append(y)
        multiNum = outputX[i] * outputY[i]
        i +=1
        if str(multiNum)[:] == str(multiNum)[::-1]:
            output.append(multiNum)
            for largNum in output:
                if largNum > output[0]:
                    output[0] = largNum
                    end.append(f"{x}*{y}")

print(f"{end[-1]}={output[0]}")
