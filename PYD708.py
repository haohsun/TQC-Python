dict1 = {}
dict2 = {}

for i,j in zip((dict1,dict2),("dict1:","dict2:")):
    print("Create "+j)
    while True:
        key = input("Key: ")
        if key == "end":
            break
        value = input("Value: ")
        i[key] = value

dict1.update(dict2)

for k in sorted(dict1.keys()):
    print(k,": ",dict1[k],sep="")