x = eval(input())
y = eval(input())
z = eval(input())

sec = x * 60 + y
hour = sec / 60 / 60
km_hr = z / hour

print("Speed = {:.1f}".format(km_hr / 1.6))