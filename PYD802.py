L = input()

total = 0

for i in L:
    print("ASCII code for '{}' is {}".format(i, int(ord(i))))
    total += int(ord(i))

print(total)