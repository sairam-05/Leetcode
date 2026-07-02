# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def recurse(root):
            if root.left is None and root.right  is None:
                return 1
            if root.left is None and root.right:
                return 1+recurse(root.right)
            if root.left  and root.right is None:
                return 1+recurse(root.left)
            if root.left and root.right:
                return min(1+recurse(root.right),1+recurse(root.left))
        return recurse(root) if root  else 0
