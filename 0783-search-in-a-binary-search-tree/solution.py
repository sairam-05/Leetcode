# Definition for a binary tree node.
# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def check(root):
            if root == None:
                return None

            if val == root.val:
                return root       
            
            if val < root.val:
                return check(root.left)
            else:
                return check(root.right)
        
        return check(root)
