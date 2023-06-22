from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        def findintersection(set1, set2):
            return [ele for ele in set1 if ele in set2]

        if len(set1) < len(set2):
            return findintersection(set1, set2)
        else:
            return findintersection(set2, set1)
