# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            else:
                return False
            
        # ✅ handle empty subRoot and empty root
        if not subRoot:                      # <-- CHANGED: added base case
            return True                      # <-- CHANGED
        if not root:                         # <-- CHANGED: added base case
            return False                     # <-- CHANGED

        # ✅ check current node, then recurse on left and right
        if root.val == subRoot.val and isSameTree(root, subRoot):  # <-- CHANGED: added isSameTree check here
            return True                                            # <-- CHANGED
        
        # ✅ try both subtrees instead of elif-chain + typo
        return (                                                  # <-- CHANGED
            self.isSubtree(root.left, subRoot) or                 # <-- CHANGED
            self.isSubtree(root.right, subRoot)                   # <-- CHANGED (also fixed isSubTree -> isSubtree)
        )
