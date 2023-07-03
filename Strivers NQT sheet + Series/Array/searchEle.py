def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print('Target Element Found', arr[i], 'On position', i)

arr = [1,2,3,4,5,6,7,8,9]
target = 9
search(arr,target)