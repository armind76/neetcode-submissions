# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self,p: Optional[TreeNode],q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.sameTree(p.left,q.left) and self.sameTree(p.right, q.right)
        else:
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: 
            return False
        elif self.sameTree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        
        
        '''
        main function:
            dfs search:
                if root and root.val == sub.val:
                    if sameTree(root, subTree):
                        return True
                elif root:
                    main(root.left,subTree)
                    main(root.right,subtree)
                else:
                    return False
        same tree(p,q):  
            base case: 
                if not q and not p:
                    return True
                elif p and q and p == q:
                    return sameTree(p.right,q.right) and sameTree(p.left,q.left)
                else:
                    return False
        '''



