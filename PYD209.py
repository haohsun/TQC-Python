x = eval(input())
y = eval(input())

# TODO
distance = (((x - 5) ** 2) + ((y - 6) ** 2)) ** 0.5

if distance <= 15:
    print("Inside")
else: 
    print("Outside")