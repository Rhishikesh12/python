def removeInplaceElement(arr):
    i = arr[0]
    j = arr[1]

    for i,j in range(len(arr)):
        
        if arr[j] != arr[i]:
            i+=1
            arr[i] = arr[j]
    return arr[i+1]

ls = [1,4,5,2,3,7,3,2,2,1,1,5]
res = removeInplaceElement(ls)
print(res)