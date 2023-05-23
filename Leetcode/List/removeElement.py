from typing import List

class Solution:
    def removeElement(self, nums: List[int],val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
    
# while val in nums:
#       nums.remove(val)
    
sol = Solution()
nums = [3,2,2,3] 
val = 3
result = sol.removeElement(nums,val)
print(result)
