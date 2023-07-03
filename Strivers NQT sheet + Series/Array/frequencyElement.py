def countFreq(list):
    mp = {}
    for x in range(len(list)):
        if list[x] in mp:
            mp[list[x]] += 1
        else:
            mp[list[x]] = 1
    
    for i in mp:
        print(i, mp[i], end="  ")


list = [1,1,3,3,3,3,2,4,4,4]
countFreq(list)