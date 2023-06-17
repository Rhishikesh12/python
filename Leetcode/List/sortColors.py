def sortColors(nums):
    l, curr, r = 0, 0, len(nums)-1
    
    while curr <= r:
        if nums[curr] == 0:
            nums[curr], nums[l] = nums[l], nums[curr]
        elif nums[curr] == 2:
            nums[curr], nums[r] = nums[r], nums[curr]
        else:
            curr+=1


nums = [2,0,2,1,0,1]