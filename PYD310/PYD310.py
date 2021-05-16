import math

n = int(input())
S = 0

for i in range(2,n+1):
   S+=1/(math.sqrt(i-1)+math.sqrt(i))
print("%.4f"%S)