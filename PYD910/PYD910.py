with open("read.dat","r",encoding = "utf-8") as file:
    for i in file:
        print(i)

males = 0
females = 0

with open("read.dat","r",encoding = "utf-8") as file:
    for i in file:
        line_sp = i.split()
        for j in line_sp:
            if j == "0":
                females += 1
            if j == "1":
                males += 1

print("Number of males:",males)
print("Number of females:",females)
