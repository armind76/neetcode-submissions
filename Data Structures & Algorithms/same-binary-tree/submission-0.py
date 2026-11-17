# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        dfs:
            def dfs(node a, node b):
                if a== None or b == None:
                    return a==b
                if a.val != b.val
                    return false
https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/e78fc10c-4692-471f-5261-61e9be4f3a00/public                dfs(a.left, b.left)
                dfs(b.right,a.right)
                return true
        '''
        def dfs (p,q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return dfs(p.right,q.right) and dfs(p.left,q.left)
            else:
                return False
        return dfs(p,q)

