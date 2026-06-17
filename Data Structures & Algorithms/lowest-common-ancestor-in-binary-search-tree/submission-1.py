# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Goal: to narrow down the search for LCA by recursing to subtrees that contain a common ancestor to both
   def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q: # Base case: root is null or p/q are null
            return None
        if (max(p.val, q.val) < root.val): # if both are <- of current root
            return self.lowestCommonAncestor(root.left, p, q) # recurse down to narrow the search
        elif (min(p.val, q.val) > root.val): # if both are -> of current root
            return self.lowestCommonAncestor(root.right, p, q) # recurse down to narrow the search
        else: # if both arent <- or ->, that means that theyre split as children on each side, or 
              # one of the p/q is teh current node. In this case, the curr node that we are at is the 
              # LCA
            return root