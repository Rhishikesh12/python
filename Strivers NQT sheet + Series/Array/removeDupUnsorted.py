# Directly converting into Set()
def removeDup(arr):
    return list(set(arr))


#  using for loop
def removeDup(arr):
    seen = set()

    for i in range (len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
    return seen


arr = [3,4,2,1,9,7,5,2,1,4,9]
res = removeDup(arr)
print(res)