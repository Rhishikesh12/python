def reverseArray(list):
    print(list[::-1])

list = [1,2,3,4,5]
reverseArray(list)
    

'''
Two-Pointer Approach

def reverseArray(arr, n):
    p1 = 0
    p2 = n - 1
    while p1 < p2:
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1
    printArray(arr, n)

'''
