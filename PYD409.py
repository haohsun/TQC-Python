nami = 0 
chopper = 0
vote = 0

for i in range(5):
    v = eval(input())
    if v == 1:
        nami += 1
    elif v == 2:
        chopper += 1
    else:
        vote += 1
    print("Total votes of No.1: Nami = ",nami)
    print("Total votes of No.2: Chopper = ",chopper)
    print("Total null votes = ", vote)

if nami > chopper:
    print("=> No.1 Nami won the election.")
elif chopper > nami:
    print("=> No.2 Chopper won the election.")
else:
    print("=> No one won the election.")