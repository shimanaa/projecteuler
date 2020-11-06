listNum = [1]
Max = 4000000

while listNum[-1] < Max:
    if len(listNum) == 1:
        test = listNum[0] + listNum[0]
        out = listNum.append(test)
    else:
        x = listNum[-1] + listNum[-2]
        if x > Max:
            break
        else:
            outPut = listNum.append(x)
            

print(listNum)