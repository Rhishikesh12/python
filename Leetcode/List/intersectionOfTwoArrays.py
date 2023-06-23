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


# Output = [3,5]


# To print [3,3,5]
def findIntersection(A, B):
    intersection = []
    i = 0
    j = 0

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1

    return intersection
