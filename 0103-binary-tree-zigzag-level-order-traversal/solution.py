# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        result = []

        if not root:
            return []

        queue = deque([root])
        level = 0
        while queue:
            levelSize = len(queue)
            level_node = []
            level += 1
            for i in range(0 , levelSize):
                current = queue.popleft()
                level_node.append(current.val)
                if current.left:
                    queue.append(current.left)
                    
                if current.right:
                    queue.append(current.right)
            
            if level % 2 == 0:
                level_node = level_node[::-1]

            result.append(level_node)
        return result
        
