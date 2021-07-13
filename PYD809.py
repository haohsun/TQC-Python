isValid = "Valid password"

pwd = input()

if len(pwd) < 8:
    isValid = "Invalid password"
if pwd.isalnum() == False:
    isValid = "Invalid password"

setAlpha = set(map(chr,range(65,91)))
setPwd = set(pwd)

if len(setAlpha & setPwd) == 0:
    isValid = "Invalid password"

print(isValid)
