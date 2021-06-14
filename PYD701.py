list1 = []

while True:
    num = eval(input())
    if num == -9999:
        break
    list1.append(num)
    
tuple1 = tuple(list1)

print(tuple1)
print("Length:",len(tuple1))
print("Max:",max(tuple1))
print("Min:",min(tuple1))
print("Sum:",sum(tuple1))