list1 = []

while True:
    s = input()
    if s == "end":
        break
    list1.append(s)

print(tuple(list1))
print(tuple(list1[:3]))
print(tuple(list1[-3:]))