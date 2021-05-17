n = eval(input())
minumum = n

while n != 9999:
    if minumum > n:
        minumum = n 
    n = eval(input())
    
print(minumum)