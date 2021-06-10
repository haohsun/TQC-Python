L = []

for i in range(10):
  L.append(eval(input()))

L.sort(reverse=True)

print(L[0],L[1],L[2])