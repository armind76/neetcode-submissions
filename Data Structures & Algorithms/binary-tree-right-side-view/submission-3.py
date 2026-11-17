# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        bfs search 
        we will append the right most element of each layer to the list 
        for a bfs search we need a queue for each level
        res []
        queue [root]
        while queue:
            length = length of q
            res.append(q[-1])
            for i in range length():  
                node = q.pop()
                if node:
                    q.append(node.left)
                    q.append(node.right)
        '''
        res = []
        q = collections.deque([root])
        
        while q:
            qLen = len(q)
            rightSide = None
            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res