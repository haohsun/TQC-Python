L = []

for i in range(10):
    L.append(eval(input()))

count = 0

for i in L:
    if L.count(i) > count:
        count = L.count(i)
        num_count = i

print(num_count)
print(count)