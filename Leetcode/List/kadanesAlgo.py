def kadaneAlgo(nums):
    sum = 0
    max = nums[0]
    for i in range(0, len(nums)):
        sum += nums[i]
        if(max < sum):
            max = sum

        if(sum < 0):
            sum = 0
    return max

nums = [-2,1,-3,4,-1,2,1,-5,4]
print("The maximum sum of Subarray is: ",kadaneAlgo(nums))