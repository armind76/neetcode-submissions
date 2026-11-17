# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
brute force solution:
    go over the tree and put each element in a list
    then finally return the k-th element 

    the way to put this stuff in an array is weird cuz how tf do we do 
    that

    dfs():
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        push left node.val
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        print(res)
        return res[k-1]
