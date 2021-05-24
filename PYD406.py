while True:
    height = eval(input())
    if height == -9999:
        break

    weight = eval(input())
    
    bmi = weight / (height / 100) ** 2
    print("BMI: {:.2f}".format(bmi))
    if bmi < 18.5:
        print("State: under weight")
    elif 18.5 <= bmi < 25:
        print("State: normal")
    elif 25.0 <= bmi < 30:
        print("State: over weight")
    elif 30 <= bmi:
        print("State: fat")