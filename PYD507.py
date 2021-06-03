def compute(n):
    if 2 > n:
        return "Not Prime"
    for i in range(2,n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"
    
a = int(input())

print(compute(a))