# TODO
n = eval(input())

if n % 3 == 0 and n % 5 == 0:
    print(n, "is a multiple of 3 and 5.")
elif n % 3 == 0 and n % 5 != 0:
    print(n, "is a multiple of 3.")
elif n % 3 != 0 and n % 5 == 0:
    print(n, "is a multiple of 5.")
else:
    print(n, "is not a multiple of 3 or 5.")