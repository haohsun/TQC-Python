def compute(x,y):
    total = 0
    for i in range(x,y+1):
        total += i
    print(total)
    
a = int(input())
b = int(input())

compute(a, b)