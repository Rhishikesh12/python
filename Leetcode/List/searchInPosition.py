def searchPosition(num, target):
    left, right = 0, len(num) - 1
    while left <= right:
        mid = (left + right) // 2
        if num[mid] == target:
            return mid
        elif num[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

nums = 1,2,5,6
target = 5
print(searchPosition(nums, target))

