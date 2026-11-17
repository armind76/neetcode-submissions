# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        count = 0
        cur val = root.val
        dfs search
            base case: 
                null kys
            if node.val > cur val:
                count ++ 
            recursive step
            node.right
            node.left
            are passed into dfs
        '''
        count = 0
        curVal = root.val
        def dfs(root, maxVal):
            nonlocal count
            if not root:
                return
            if root.val >= maxVal:
                count += 1
            maxVal = max(root.val,maxVal)
            print(root.val)
            dfs(root.left,maxVal)
            dfs(root.right,maxVal)
        dfs(root,root.val)
        return count 
        







