x = []
y = []

for i,j in zip((x,y),("X's","Y's")):
    print("Enter group "+j+" subjects:")
    while True:
        subject = input()
        if subject == 'end':
            break
        i.append(subject)

print(sorted(list(set(x)|set(y))))
print(sorted(list(set(x)&set(y))))
print(sorted(list(set(y)-set(x))))
print(sorted(list(set(x)^set(y))))
