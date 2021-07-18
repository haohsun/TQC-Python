f_name = input()
str_old = input()
str_new = input()

with open(f_name,"r",encoding ="utf-8") as file:
    content = file.read()
print("=== Before the replacement")
print(content)

content = content.replace(str_old,str_new)

with open(f_name,"w",encoding ="utf-8") as file:
    file.write(content)
print("=== After the replacement")
print(content)