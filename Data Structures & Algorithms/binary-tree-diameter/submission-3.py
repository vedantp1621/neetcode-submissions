# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # how to find the diameter of a binary tree
        # 

        best = 0

        def dfs(root):
            nonlocal best

            if not root: 
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
        
            best = max(best, left + right) # global tracker of the best height
            
            return 1 + max(left, right) # EXTENDIBLE height the parent is using
            

        dfs(root)
        return best