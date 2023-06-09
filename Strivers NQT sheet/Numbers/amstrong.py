def isAmstrong(num):
    size = len(str(num))
    res = 0
    temp = num    

    while(num > 0):
        ans = num % 10
        res += ans**size
        num = num // 10
        
    return res == temp

num = 3
res = isAmstrong(num)
if(res == True):
    print("Amstrong Number")
else:
    print("Not Amstrong Number")