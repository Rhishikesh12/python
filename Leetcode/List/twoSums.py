from typing import List

#  O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]


# O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for idx, value in enumerate(nums):
            if target - value in values:
                return [values[target-value],idx]
            else:
                values[value] = idx
    

                
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)
