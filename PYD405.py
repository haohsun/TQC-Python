fraction = eval(input())

while fraction != -9999:

    if fraction == 100 or fraction > 89:
        print("A")
    elif fraction ==89 or fraction > 79:
        print("B")
    elif fraction ==79 or fraction > 69:
        print("C")
    elif fraction ==69 or fraction > 59:
        print("D")
    else:
        print("E")
    fraction = eval(input())
