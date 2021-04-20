a = eval(input())
total = 0

for i in range(1,a+1):
    if i % 5 == 0:
        total += i

print(total)
