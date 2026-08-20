# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
            
        s = [(root, root.val)]
        while s:
            
            curr, curr_total = s.pop()

            if curr_total == targetSum and not curr.left and not curr.right:
                return True
            
            if curr.left:
                s.append((curr.left, curr_total + curr.left.val))
            if curr.right:
                s.append((curr.right, curr_total + curr.right.val))

        return False