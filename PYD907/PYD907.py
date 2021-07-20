# TODO
L, W, C = 0, 0, 0

file_name = input()

file = open(file_name,"r",encoding = "utf-8")

for line in file:
    L += 1
    line_sp = line.split()
    W += len(line_sp)
    for i in range(len(line_sp)):
        C += len(line_sp[i])
    
file.close()
    
print(L,"line(s)")
print(W,"word(s)")
print(C,"character(s)")
