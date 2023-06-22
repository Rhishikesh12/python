class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self,A):
        slow = A[0]
        fast = A[0]

    # Move slow and fast pointers until they meet
        while True:
            slow = A[slow]
            fast = A[A[fast]]
            if slow == fast:
                break

    # Reset slow pointer to the first element
        slow = A[0]

    # Move both pointers one step at a time until they meet again
        while slow != fast:
            slow = A[slow]
            fast = A[fast]

        return slow


# Used Cycle Detection Algorithm. / slow-pointer,fast-pointer