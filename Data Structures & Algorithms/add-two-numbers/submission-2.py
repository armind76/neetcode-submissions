# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cary = 0
        c1 = l1
        c2 = l2
        head = ListNode()
        copy = head
        while c1 and c2:
            s = c1.val + c2.val + cary
            if s >= 10:
                cary = 1
                s = s % 10
            else:
                cary = 0
            
            copy.next = ListNode(val = s)
            copy = copy.next
            c1 = c1.next
            c2 = c2.next
        while c1:
            s = cary + c1.val
            cary = s//10
            s = s%10

            copy.next = ListNode(val = s)
            copy= copy.next
            c1 = c1.next
        while c2:
            s = cary + c2.val
            cary = s//10
            s = s%10
            copy.next = ListNode(val = s)
            copy= copy.next
            c2 = c2.next
        if cary == 1:
            copy.next = ListNode(val = 1)


        return head.next