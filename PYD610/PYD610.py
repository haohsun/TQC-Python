week_1 = []
week_2 = []
week_3 = []
week_4 = []

for i,j in zip((week_1,week_2,week_3,week_4), range(1,5)):
    print("Week "+str(j)+":")
    for k in range(1,4):
        i.append(eval(input('Day %d:' %(k))))

total = week_1 + week_2 + week_3 + week_4

print("Average: {:.2f}".format(sum(total) / len(total)))
print("Highest:",max(total))
print("Lowest:",min(total))

"""
L=[]
for w in range(1,4+1):
  print("Week %d:"%w)
  for D in range(1,3+1):
    x=eval(input("Day %d:"%D))
    L.append(x)
 
A=sum(L)/len(L)
print("Average: %.2f"%A)
print("Highest:",max(L))
print("Lowest:",min(L))

"""