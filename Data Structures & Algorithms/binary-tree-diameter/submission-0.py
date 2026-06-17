# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ESSENTIAL PYTHON CONCEPT, NESTED FUNCTIONS
class Solution:
    # Logic of this solution: we will add the left branch height and right branch height for each 
    # node in the tree. By adding these heights, adn tracking the max recorded added height for
    # any node here, we essentially find the largest path
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 # var to track the combined heights globally. by having this global, we can track
                # the last max that was recorded

        def dfs(root): # helper function that will recurse as we perform a DFS
            nonlocal res # nonlocal: references the last contexts variable (res in the outer func)

            if not root: # base case: we are at a null reference and dont need to count this one
                return 0
            left = dfs(root.left) # recurse left
            right = dfs(root.right) # recurse right
            res = max(res, left + right) # update res to the max between res
                                         # and the current left + right of THIS node

            return 1 + max(left, right) # add this one and the children heights

        dfs(root) # start the recursion
        return res # return the last highest res value