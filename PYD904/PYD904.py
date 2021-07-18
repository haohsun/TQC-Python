name, height, weight, data = [],[],[],[]

with open("read.txt","r") as file:
    for line in file:
        print(line)
        data = line.replace("\n","").split(" ")
                
        name.append(data[0])
        height.append(int(data[1]))
        weight.append(int(data[2]))
    
print("Average height: %.2f" %(sum(height) / len(height)))
print("Average weight: %.2f" %(sum(weight) / len(weight)))

tallest = height.index(max(height))
print("The tallest is {} with {:.2f}cm".format(name[tallest], height[tallest]))

heaviest = weight.index(max(weight))
print("The heaviest is {} with {:.2f}kg".format(name[heaviest],weight[heaviest]))
