# https://youtu.be/jL3QcVLqjs0


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range (1, len(nums)):
            if nums[i] != nums[j]:
                j+=1
                nums[j] == nums[i]
        return j+1

nums = [1,1,2]
res = Solution().removeDuplicates(nums)
print(res)