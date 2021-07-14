f = open("read.txt","r")

s = map(int,f.read().split(" "))

f.close()

print(sum(s))