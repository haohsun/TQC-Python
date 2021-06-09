cards = ["0","A","2","3","4","5","6","7","8","9","10","J","Q","K"]

total = 0

for i in range(5):
    num = input()
    total += cards.index(num)

print(total)