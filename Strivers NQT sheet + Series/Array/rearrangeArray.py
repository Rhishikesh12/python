def rearrange_Array(arr):
    arr.sort()
    mid = len(arr) // 2
    first = arr[:mid]
    sec = arr[mid:]
    sec_rev = sec[::-1]
    res = first + sec_rev
    return res

arr = [8,7,1,6,5,9]
res = rearrange_Array(arr)
print(res)


'''
Sort the array in ascending order.
Determine the midpoint of the array.
Split the array into two halves: the first half from index 0 to the midpoint (exclusive), and the second half from the midpoint to the end of the array.
Reverse the second half of the array.
Combine the first half and the reversed second half to get the desired output.
'''