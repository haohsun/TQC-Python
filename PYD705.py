set1 = set()
set2 = set()
set3 = set()

for i,j,k in zip((set1,set2,set3),(5,3,9),range(1,4)):
    print("Input to set{}:".format(k))
    for h in range(j):
        i.add(eval(input()))
        
print("set2 is subset of set1:",set2 <= set1)
print("set3 is superset of set1:",set3 >= set1)