f_name = input()
string = input()

with open(f_name, "r", encoding = "utf-8") as file:
    content = file.read()

print("=== Before the deletion")
print(content)

content = content.replace(string,"")

with open(f_name, "w", encoding = "utf-8") as file:
    file.write(content)    
print("=== After the deletion")
print(content)