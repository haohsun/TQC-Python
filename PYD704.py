set1 = set()

while True:
    num = eval(input())
    if num == -9999:
        break
    set1.add(num)

print("Length:",len(set1))
print("Max:",max(set1))
print("Min:",min(set1))
print("Sum:",sum(set1))