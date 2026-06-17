# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1

        if right > left:
            return right
        else: return left
        '''
        end each branch by returning greatest of left side vs right side
        go left first
        then go right
        '''
        