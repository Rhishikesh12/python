def isPrime(num):

    for i in range(1,100):
        if num % i == 0:
            return False
    return True





number = 6
res = isPrime(number)
if res == True:
    print("Number is Prime")
else:
    print("Number is not Prime")