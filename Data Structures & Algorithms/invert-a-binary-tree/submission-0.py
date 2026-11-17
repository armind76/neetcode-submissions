# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
recursive algorithm
in the main function
recursive (root)
    recursive(node):
    recursive step:
        if null return
    recursive(left)
    recursive(right)
    left,right = right,left
    # a = temp
    # a = b
    # b = temp
return root

'''

class Solution:
    def recursive(self, node):
        if node == None:
            return None
        self.recursive(node.left)
        self.recursive(node.right)
        node.left,node.right = node.right,node.left
        return node
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.recursive(root)
        