# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        so dfs
        recursive function
        base case:
            return true if both are null
        recursive case:
            if a.value == b.value:
                return dfs(a.left,b.left) and dfs(a.right, b.right)

        '''
        def dfs(p,q):
            if not p and not q:
                return True
            elif p and q and p.val == q.val:
                return dfs(p.left,q.left) and dfs(p.right,q.right)
            else:
                return False

        return dfs(p,q)
            
