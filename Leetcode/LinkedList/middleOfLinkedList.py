# approach slow and fast pointer
def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# other approach : 
'''
1) count the total number of nodes and divide them by 2 : (n/2)
2) whatever result we get add + 1 to it.

that's your middle element

'''