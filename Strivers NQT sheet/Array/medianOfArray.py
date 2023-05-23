def findMedian(arr):
    #  sorted = sorted(arr)             // we can also use this method
    arr.sort()
    n = len(arr)
    if (n % 2 == 0):
        a = (n // 2) - 1
        b = (n // 2)
        median = (arr[a] + arr[b] /2)
    else: 
        median = (arr[n//2])
    return median

arr = [2,4,1,3,5]
res = findMedian(arr)
print(res)


'''

To find the median of an unsorted array in Python, you can follow these steps:

Sort the array in ascending order.
Determine the length of the array.
If the length is odd, return the middle element.
If the length is even, return the average of the two middle elements.


'''