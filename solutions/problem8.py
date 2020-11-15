def result(var):
    for x in range(1,var):
        for y in range(1,var - x):
            c = var - x - y
            if x**2 + y**2 == c**2:
                print(x,y,c)
                return


result(1000)
