def compute(m,n):
    if n == 0:
        return m
    else:
        return compute(n, m%n)
    
a,b = eval(input())

print(compute(a,b))