# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
step 1: keep track of next
set 2: make cur.next = prev
step3: set prev to cur
'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

