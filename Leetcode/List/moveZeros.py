from typing import List, Self


class Solution:
    def moveZeroes(self, nums: List[int]) -> List:
        n = len(nums)
        count = 0
        
        #count karo ki zeros kitne he array me
        for i in range(n):
            if nums[i] == 0:
                count +=1
        
        # sab non-zero ele ko aage leke aao order se
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j+=1
        
        # baaki ke bache hue boxes ki value 0 kardo
        for i in range (j,n):
            nums[i] = 0

        return nums
        
    nums = [0,1,3,0,0,12]
    print(moveZeroes(Self,nums))