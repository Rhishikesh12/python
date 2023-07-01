# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        mid = self.middle(head)
        reverse = self.reverse(mid)

        while reverse:
            if head.val != reverse.val:
                return False
            head = head.next
            reverse = reverse.next
        return True


    def reverse(self, node):
        curr = node
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


    def middle(self, head):
        slow = fast = head

        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
