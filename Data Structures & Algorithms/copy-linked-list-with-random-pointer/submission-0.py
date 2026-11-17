"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {}
        dum = Node(0)
        copy = dum
        cur = head
        while cur:
            if cur.random not in mp:
                if cur.random:
                    mp[cur.random] = Node(cur.random.val)
                    print (cur.random.val)
                else:
                    mp[cur.random] = None
            if cur in mp:
                copy.next = mp[cur]
            else:        
                copy.next = Node(cur.val)
                mp[cur] = copy.next
            copy.next.random = mp[cur.random]
            copy = copy.next
            cur= cur.next
        return dum.next
        