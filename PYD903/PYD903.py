with open('data.txt','a',encoding='UTF-8') as fp:
  for i in range(5):
    fp.write("\n"+input())
 
print('Append completed!')
print('Content of "data.txt":')
 
with open('data.txt','r',encoding='UTF-8') as fp:
  for line in fp:
    print(line,end="")