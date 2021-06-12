def compute(x,y):
    for i in range(x):
        for j in range(y):
            print("{:4d}".format(j-i),end = "")
        print()
        
rows = int(input())
cols = int(input())

compute(rows,cols)
