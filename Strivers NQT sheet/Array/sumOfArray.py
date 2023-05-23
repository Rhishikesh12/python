def sumOfarray(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

arr = [1,2,3,4,5]
res = sumOfarray(arr)
print(res)