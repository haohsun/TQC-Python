dict1 = dict()

while True:
    key = input("Key: ")
    if key == "end":
        break
    value = input("Value: ")
    dict1[key] = value

search = input("Search key: ")

print(search in dict1)