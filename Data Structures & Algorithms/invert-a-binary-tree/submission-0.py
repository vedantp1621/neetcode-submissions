# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None # base case, we return None if there are no children
        
        self.invertTree(root.left) # visit left first, goes all the way down (DFS)
        self.invertTree(root.right) # then visit right
        root.left, root.right = root.right, root.left # then swap, should swap on the way up

        return root # at the end, all swaps are made and we can return root




