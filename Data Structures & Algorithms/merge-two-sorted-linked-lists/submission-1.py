# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
res
cur = res.next
list 1 and list 2
while 1 != None and 2 != None
if 1[i]<=2[i]:
    res.next = 1[i]
else:
    res.next = 2[i]

if 1 != None:
    res.next = 1
if 2 != None:
    res.next = 2
return res.next


'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = curr = ListNode()
        dummy = ListNode()
        while list1 != None and list2 != None: 
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return res.next
                
        





