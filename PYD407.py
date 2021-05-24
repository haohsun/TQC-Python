while True:
    year = int(input())
    if year == -9999:
        break
    if year % 400 == 0:
        print(year,"is a leap year.")
    elif year % 4 == 0 and year % 100 != 0:
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")