list1 = []
list2 = []

for i,j in zip((list1,list2), range(1,3)):
    print("Create tuple"+str(j)+":")
    while True:
        num = eval(input())
        if num == -9999:
            break
        i.append(num)

print("Combined tuple before sorting:",tuple(list1 + list2))

total = list1 + list2
total.sort()
print("Combined list after sorting:",total)