# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        foundp, foundq = False, False
        que = deque([root])
    
        while que:
            curr = que.popleft()

            if p.val <= curr.val <= q.val or q.val <= curr.val <= p.val:
                return curr
            else:
                que.append(curr.left)
                que.append(curr.right)