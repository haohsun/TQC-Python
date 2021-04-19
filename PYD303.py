n = int(input())

for i in range(1,n+1):
    for j in range(1,i+1):
        print("{:>4d}".format(j * i),end="")
    print()