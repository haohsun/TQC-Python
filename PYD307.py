n = int(input()) #小於10

for i in range(1, n+1):
    for j in range(1, n+1):
        print("{} * {} = {:<4}".format(j,i,i*j),end = "")
    print()