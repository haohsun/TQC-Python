f_name = input()
n = int(input())

with open(f_name,"r",encoding = "utf-8") as file:
        all_word = file.read().split()

words = []

file = open(f_name,"r",encoding = "utf-8")

for line in file:
    line_sp = line.split()
    for word in line_sp:
        if all_word.count(word) == n:
            words.append(word)

words = list(set(words))
words.sort()

for i in words:
    print(i)
    
file.close()