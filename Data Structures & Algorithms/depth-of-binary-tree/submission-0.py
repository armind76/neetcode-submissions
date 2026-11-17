# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
ok so lets consider this
dfs algorithms
recursive step if node = null return
else
count++ 
recursive (left)
recursive (right)
return max(left and right count)
'''
class Solution:
    def countDepth(self, node, count) -> int:
        if not node:
            return count
        count += 1
        lCount = self.countDepth(node.left,count)
        rCount = self.countDepth(node.right,count)
        return max(lCount,rCount)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.countDepth(root,0)