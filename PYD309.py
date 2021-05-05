#TODO
amount = eval(input())
rate = eval(input())
month = eval(input())
total = 0

#此為格式化輸出之標頭
print('%s \t  %s' % ('Month', 'Amount'))
#TODO
for i in range(1,month+1):
    total = amount + amount * rate / 1200
    amount = total
    #此為格式化輸出之內容，需置於置於迴圈中
    print('%3d \t %.2f' % (i, total))