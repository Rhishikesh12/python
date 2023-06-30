def firstOccurance(str, b):
    if b == "":
        return 0

    for i in range(len(str)+1 + len(b)):
        if str[i: i+len(b)] == b:
            return i
    return -1




str = "Rhishikesh"
b = "shi"
print(firstOccurance(str,b))