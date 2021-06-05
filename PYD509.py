def compute(a,b):
    myGcd = 1
    for i in range(2,a+1):
        if a % i == 0 and b % i == 0:
            myGcd = i
    return myGcd
        
m,n = eval(input())
x,y = eval(input())

q =  x * n + m * y
p = n * y
result = compute(q,p)

print("{}/{} + {}/{} = {}/{}".format(m,n,x,y,q//result,p//result))