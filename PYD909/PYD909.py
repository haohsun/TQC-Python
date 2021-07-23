with open("data.dat","w",encoding="UTF-8") as file:
    for i in range(5):
        file.write(input()+"\n")

print('The content of "data.dat":')

with open("data.dat","r",encoding="utf-8") as file:
    for i in file:
        print(i)