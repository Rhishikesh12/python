
# Linearly traverse both the linked-lists and when any one of them reaches to Null switch the pointer to other list's head.
 
def intersectionLinkedlist(headA, headB):
    if headA == None or headB == None:
        return None

    a = headA
    b = headB

    while a!=b:
        a = headA if a is None else a.next
        b = headB if b is None else b.next
    return a