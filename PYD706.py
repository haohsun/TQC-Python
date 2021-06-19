times = int(input())

for i in range(times):
    text = set(input())
    count = 0
    for j,k in zip((range(65,91)),(range(97,123))):
        if chr(j) in text or chr(k) in text:
            count += 1
    print(count == 26)
