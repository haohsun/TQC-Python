# TODO
times = eval(input())

for w in range(times):
    number = input()
    total = 0 

    for i in range(len(number)):
        total += int(number[i])
    print("Sum of all digits of " + number + " is", total)


"""
Sum of all digits of _ is _
"""