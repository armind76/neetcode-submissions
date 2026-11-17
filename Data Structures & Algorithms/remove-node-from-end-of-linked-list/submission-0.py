# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        size = 0
        while cur: 
            size += 1
            cur = cur.next
        index = size - n  
        if index == 0:
            return head.next
        cur = head
        i = 0
        while i < index - 1:
            cur = cur.next
            i += 1
        cur.next = cur.next.next
        return head

        
