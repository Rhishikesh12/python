def isPalindrome(num):
    return str(num) == str(num)[::-1]

def palindromeInRange(min,max):
    palNums = []
    for i in range(min,max+1):
        if isPalindrome(i):
            palNums.append(i)
    return palNums
        
min,max = 10,50
print(palindromeInRange(min,max))