def lastWord(str):
    i, length = len(str) -1, 0
    while str[i] == " ":
        i-=1
    while i >= 0 and str[i] != " ":
        length +=1
        i-=1
    return length

str = "  this is fun"
print(lastWord(str))