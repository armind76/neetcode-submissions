# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
my idea is that we store each node inside an array of length, size and then we go from there
if n % 2 == 0:
    cur.next == n - (1 + (n//2)) # at index
else:
    cur.next == n // 2 

now we need to figure out how to know when we are at the end of the list


'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        arr = list()
        while cur != None:
            arr.append(cur)
            cur = cur.next
        i,j = 0,len(arr)- 1
        while i < j:
            arr[i].next = arr[j]
            i += 1
            if i >= j:
                break;
            arr[j].next = arr[i]
            j -= 1
        arr[i].next = None
        
        
        