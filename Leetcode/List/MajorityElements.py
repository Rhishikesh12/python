class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        candidate = A[0]
        count = 1

    # Find the candidate for majority element
        for i in range(1, len(A)):
            if A[i] == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = A[i]
                    count = 1

        return candidate