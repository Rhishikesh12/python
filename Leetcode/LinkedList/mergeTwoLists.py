# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases: if either list is empty, return the other list
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # Recursive cases: merge the lists based on the node values
        if list1.val <= list2.val:
            merged = list1
            merged.next = self.mergeTwoLists(list1.next, list2)
        else:
            merged = list2
            merged.next = self.mergeTwoLists(list1, list2.next)

        return merged



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2 ):
        # Create a dummy node as the head of the merged list
        dummy = ListNode()
        merged = dummy

        # Initialize pointers to the heads of list1 and list2
        ptr1, ptr2 = list1, list2

        # Iterate while both pointers are not None
        while ptr1 and ptr2:
            # Compare the values at the current nodes
            if ptr1.val <= ptr2.val:
                # Connect the smaller node to the merged list
                merged.next = ptr1
                ptr1 = ptr1.next
            else:
                merged.next = ptr2
                ptr2 = ptr2.next

            # Move the merged pointer forward
            merged = merged.next

        # Append the remaining nodes from list1 or list2
        if ptr1:
            merged.next = ptr1
        elif ptr2:
            merged.next = ptr2

        # Return the head of the merged list (next node of the dummy node)
        return dummy.next
