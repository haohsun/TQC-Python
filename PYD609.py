
'''
list1 = []
list2 = []
total_list = []

for i,h in zip((list1,list2),range(1,3)):
    print("Enter matrix {}:".format(h))
    for j in range(1,3):
        for k in range(1,3):
            i.append(eval(input('[%d, %d]: '%(j,k))))

for i,j in zip(range(1,3),(list1,list2)):
    print("Matrix {}:".format(i))
    print("{} {}".format(j[0],j[1]))
    print("{} {}".format(j[2],j[3]))

for i in range(4):
    total_list.append(list1[i]+list2[i])

print("Sum of 2 matrices:")
print("{} {}".format(total_list[0],total_list[1]))
print("{} {}".format(total_list[2],total_list[3]))
'''

L1 = [[0 for i in range(2)] for j in range(2)]
L2 = [[0 for i in range(2)] for j in range(2)]
 
print('Enter matrix 1:')
for i in range(2):
    for j in range(2):
        L1[i][j] = int(input('[%d, %d]: '%(i+1,j+1)))
 
print('Enter matrix 2:')
for i in range(2):
    for j in range(2):
        L2[i][j] = int(input('[%d, %d]: '%(i+1,j+1)))
 
print('Matrix 1:')
for i in range(2):
    for j in range(2):
      print(L1[i][j],end=' ')
    print()
 
print('Matrix 2:')
for i in range(2):
    for j in range(2):
      print(L2[i][j],end=' ')
    print()
 
print('Sum of 2 matrices:')
for i in range(2):
    for j in range(2):
      print((L1[i][j]+L2[i][j]),end=' ')
    print()