# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # recursive function, returns [boolean, integer]. the boolean states whether the tree
        # is balanced at the root, and the integer states the height of the tree.
        def dfs(root):
            if not root: # base case: the node is null so we are not counting it in the height
                return [True, 0] # return 0 and keep balanced state

            left, right = dfs(root.left), dfs(root.right) # we traverse down to the children nodes
            # the following code is related to calculating the heights of nodes below the current
            # node. balanced checks if the tree is still balanced, in which case we return that status
            # and then also include the maximum height
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1 # in each node, we want to 
                                                                        # to calculate the balanced 
                                                                        # state, and the height rule
            return [balanced, 1 + max(left[1], right[1])] # calculate the new height to be recorded,
                                                          # should be the heighest betweeen the two
                                                          # children

        return dfs(root)[0] # return the height recorded at the root
 

