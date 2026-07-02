# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return
            vals.add(node.val)
            dfs(node.left)
            dfs(node.right)
        vals=set()
        dfs(root)
        return -1 if len(vals)<2 else sorted(vals)[1]
