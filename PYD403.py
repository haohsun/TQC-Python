a = eval(input())
b = eval(input())
count = 0
total = 0

for i in range(a, b+1):
    if i % 4 == 0 or i % 9 == 0:
        print("{:<4d}".format(i),end = "")
        total += i
        count += 1
        if count % 10 == 0:
            print()
print()
print(count)
print(total)