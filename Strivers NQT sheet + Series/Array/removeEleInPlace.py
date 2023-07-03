
# Only work for Sorted array
def removeInplaceElement(arr):
    i = 0

    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i+1

arr = [1,1,1,1,2,2,2,3,3,4,4,4,4,4]
k = removeInplaceElement(arr)
print("The array after removing duplicate elements is ")
for i in range(k):
    print(arr[i], end=" ")


'''
using Two_Pointer Approach 

we have kept i = 0 and j = 1
and started iterating from 1 till n-1

will will keep visiting next element until the element which is not equal to i
we will increment the i pointer and update the arr[i] = arr[j]

'''
