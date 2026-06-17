# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0 # Base case: if the current is None, it should not be added 
                                  # to the depth
        
        left = self.maxDepth(root.left) + 1 # add this one and go left
        right = self.maxDepth(root.right) + 1 # add this one and go right

        if right > left: # if the left chain is less than the right chain, we will return right
                         # otherwise we will return the sum of the left
            return right
        else: return left
        '''
        end each branch by returning greatest of left side vs right side
        go left first
        then go right
        '''
        