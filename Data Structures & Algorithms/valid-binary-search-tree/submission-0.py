# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# If you draw it out, this solution is quite trivial

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right): # recursive func to handle propagating downward 
            if not node: # base case, if we got here there were no issues
                return True
            if not (left < node.val < right): # case to track any issues and break the entire 
                                              # call stack
                return False

            # when we descend left, we want to find something < than last value and greater than whatever
            # was last set as left

            # when we descend right, we want to find something > than last value and less than whatever was
            # last set as right

            # therefore, we change left only when going right, and vis versa
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf")) # init the call stack. the float funcs return the 
                                                        # greatest/smallest floats