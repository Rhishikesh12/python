def perfectNumber(num):
    res = 0
    for i in range(1,num):
        if num % i == 0:
            res += i
    return res == num


num = 28
res = perfectNumber(num)
if res:
    print("Perfect Number")
else:
    print("Not perfect Number")