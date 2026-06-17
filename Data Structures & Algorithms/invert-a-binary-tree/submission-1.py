# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # id imagine you create a new tree.
        # as you iterate through the first tree, you create the second, but inverted

        # or are we doing this 'in-place' where you are swapping pters

        if not root:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root