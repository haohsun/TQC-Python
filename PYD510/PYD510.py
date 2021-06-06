"""
def compute(n):
    
    x = 0 
    y = 1
    
    for i in range(n):
        print(x,end = " ")
        x, y = y, x + y
        
num = int(input())

compute(num)
"""
def compute(i):
    if i <= 1:
        return i
    else:
        return compute(i-1) + compute(i-2)
    
num = int(input())

for i in range(num):
    print(compute(i),end = " ")