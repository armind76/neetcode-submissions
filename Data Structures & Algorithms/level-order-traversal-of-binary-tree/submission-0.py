# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        implement a bfs traversal 
        res []
        que [root]
        while que:
            qLen = len(que)
            tmp =[]
            for i in range(qlen):
                if node:
                    tmp.append(node)
                    que.push(node.left)
                    push node.right
                if tmp:
                    res.append(tmp)
        '''
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            qLen = len(q)
            tmp = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    tmp.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if tmp:
                res.append(tmp)
        return res 