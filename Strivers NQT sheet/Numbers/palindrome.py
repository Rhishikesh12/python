def palindromeORnot(num):
    nums = list(str(num)) 
    i, j = 0 , len(nums)-1
    while i < j:
        if nums[i] != nums[j]:
            return False
        i += 1
        j -= 1
    return True


number = 101
res = palindromeORnot(number)
if res == True:
    print("Number is palindrome")
else:
    print("Number is not palindrome")