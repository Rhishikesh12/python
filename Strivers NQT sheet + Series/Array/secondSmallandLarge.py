# first approach
# Sort the array in ascending order
# The element present at the second index is the second smallest element
# The element present at the second index from the end is the second largest element

# Second Approach 
# O(n)
def second_small(arr):
    
    smlest = float('inf')
    sec_small = float('inf')
    lrgest = float('-inf')
    sec_large = float('-inf')

    for i in range(len(arr)):
        if arr[i] < smlest:                         # if smallest is less than current element
            sec_small = smlest                      # then it will obviously second smallest
            smlest = arr[i]                         # and new small value is assigned to Smallest
        elif arr[i] < sec_small and arr[i] != smlest:       # current value should not be equal to smallest and should be less than second small 
            sec_small = arr[i]                      # assign to the second small if current value is less than that.

        if arr[i] > lrgest:
            sec_large = lrgest
            lrgest = arr[i]
        elif arr[i] > sec_large and arr[i] != lrgest:
            sec_large = arr[i]
    return sec_small,sec_large
    

arr = [1,2,3,6,4,3,7,9]
small, large = second_small(arr)
print('Second Small', small)
print('Second Large', large)


