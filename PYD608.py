list1 = []

for i in range(9):
    list1.append(eval(input()))

max_index = list1.index(max(list1))
min_index = list1.index(min(list1))

print("Index of the largest number {} is: ({}, {})"
      .format(max(list1),max_index//3,max_index%3))
print("Index of the smallest number {} is: ({}, {})"
      .format(min(list1),min_index//3,min_index%3))