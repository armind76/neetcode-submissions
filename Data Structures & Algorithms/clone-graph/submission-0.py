"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        there has to be something missing cuz lord idfk what the hard part of ts is

        we go over the list, we add each element to a q,
        then we (try to) add the node to a map,
        if node is in the set we dont add it to the end of the queue elsee we do add it to the en
        of the queue
        

        ok so it wasnt easy but it wasnt that hard either, i just needed a map its a lil complex so lets go
        '''
        if not node:
            return None

        oldToNew = {}
        qu = deque([node])
        oldToNew[node] = Node(node.val)
        while qu:
            cur = qu.popleft()
            for n in cur.neighbors:
                if n not in oldToNew:
                    oldToNew[n] = Node(n.val)
                    qu.append(n)
                oldToNew[cur].neighbors.append(oldToNew[n])
                
        return oldToNew[node]