#f_name = input()
n = 3

with open("/Users/lihaohsun/Desktop/桌面 2/GitHub/TQC-Python/PYD908/read.txt"
            ,"r",encoding = "utf-8") as file:
        all_word = file.read().split()

words = []

file = open("/Users/lihaohsun/Desktop/桌面 2/GitHub/TQC-Python/PYD908/read.txt"
            ,"r",encoding = "utf-8")

for line in file:
    line_sp = line.split()
    for word in line_sp:
        if all_word.count(word) == n:
            words.append(word)

words = list(set(words))
words.sort()

for i in words:
    print(i)