def rotateString(str,strB):
    if len(str) != len(strB):
        return False
    
    concate = str + str

    if strB in concate:
        return True


str = "Rhishikesh"
strB = "ishikeshR"

print(rotateString(str,strB))