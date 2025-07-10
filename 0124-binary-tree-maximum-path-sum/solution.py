# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=root.val
        def rec(root):
            if root==None:
                return 0
            ls=rec(root.left)
            rs=rec(root.right)
            curvesum=root.val+ls+rs
            nodesum=max(root.val,root.val+max(ls,rs))
            self.maxi=max(self.maxi,curvesum,nodesum,root.val)
            return nodesum
        rec(root)
        return self.maxi
