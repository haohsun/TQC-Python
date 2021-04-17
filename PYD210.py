side1 = eval(input())
side2 = eval(input())
side3 = eval(input())

perimeter = side1 + side2 + side3 
#TODO
if side1 + side2 > side3 and side3 + side2 > side1 and side1 + side3 > side2:
    print(perimeter)
else:
    print("Invalid")



"""
Invalid
"""