L = list()

for i in range(10):
    L.append(eval(input()))
    
L.sort()
    
print(sum(L[1:9]))
print("{:.2f}".format(sum(L[1:9]) / len(L[1:9])))