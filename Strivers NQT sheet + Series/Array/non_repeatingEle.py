def non_repeatingElement(arr):
    dic = {}
    rep_ele = []

    for i in range(len(arr)):
        if arr[i] in dic:
            dic[arr[i]] += 1    # incrementing count
        else:
            dic[arr[i]] = 1
    
    for ele, count in dic.items():
        if count == 1:
            rep_ele.append(ele)
    return rep_ele

arr = [1,2,-1,1,3,1]
res = non_repeatingElement(arr)
print(res)