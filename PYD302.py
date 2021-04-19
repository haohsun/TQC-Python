# TODO
a = eval(input())
b = eval(input())
c = 0

for i in range(a, b+1):
    if i % 2 == 0:
        c += i
print(c)
