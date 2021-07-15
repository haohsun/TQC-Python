fp = open("write.txt","w",encoding ="utf-8")

for i in range(5):
    fp.write(input())
    fp.write("\n")
    
fp.close()