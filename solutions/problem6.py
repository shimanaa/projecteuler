re = 0
output = 0
for x in range(1,11):
    re += x * x
    output += x 
    result = output * output

print(f"{result}-{re}=>{result-re}")
