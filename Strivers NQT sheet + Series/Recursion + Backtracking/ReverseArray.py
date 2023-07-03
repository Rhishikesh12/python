# * Using Two Pointer
def revArray(arr, l, r):
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    return revArray(arr, l+1, r-1)

# * Using One Single Pointer
def revArray(arr, i, size):
    if i >= size/2:
        return
    arr[i], arr[size-i-1] = arr[size-i-1], arr[i]
    return revArray(arr, i+1, size)

# * Passing Parameters and Printing Output Here
arr = [1,2,3,4]
for i in range(len(arr)):
    print(arr[i], end=" ")
# revArray(arr, 0, len(arr)-1)
revArray(arr, 0, len(arr))
print()
for i in range(len(arr)):
    print(arr[i], end=" ")
