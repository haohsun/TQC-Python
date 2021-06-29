num = input().replace("-","") #把使用者輸入的 - 取代成無

if(num.isdigit()): #是否為數字
  print('Valid SSN')  #有效
else:
  print('Invalid SSN')#無效