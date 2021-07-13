times = int(input())

for i in range(times):
    num = list(map(float,input().split(" "))) 
    print("{:.2f}".format((max(num)) - (min(num))))