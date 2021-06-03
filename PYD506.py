def compute(a,b,c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        s = "Your equation has no root."
    
    elif d == 0:
        ans = -b / 2*a
        s = str(ans)
    else:
        ans1 = (-b + d ** 0.5) / (2 * a)
        ans2 = (-b - d ** 0.5) / (2 * a)
        s = str(ans1) + ", " + str(ans2)
    return s

a = eval(input())
b = eval(input())
c = eval(input())

print(compute(a,b,c))
