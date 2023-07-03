def revString(strn, i):
    if i >= len(strn)/2:
        return True
    if strn[i] is not strn[len(strn)-i-1]:
        return False
    return revString(strn, i+1)


strn = str(input(" Enter String : "))
strn = strn.lower()
res = revString(strn, 0)
if res:
    print("Palindrome")
else:
    print("Not a Palindrome")