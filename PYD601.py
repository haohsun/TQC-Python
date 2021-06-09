number_List = []
total = 0

for i in range(12):
    num = int(input())
    number_List.append(num)
    if i % 2 == 0:
        total += number_List[i]
count = 0   
for i in number_List:
    print("{:>3d}".format(i),end="")
    count += 1
    if count % 3 ==0:
        print()
        
print(total)
