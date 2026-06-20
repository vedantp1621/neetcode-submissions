# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # pattern here is a traversal down where you need the prev nodes value
        # create a dfs function that takes the value of the caller node as its parameter
        # use that value to determine if the mode being visited in the callee has a value greater or less
        # then track a global counter to see the total count of good nodes
        def dfs(node, max_so_far): # tracks running max down to children
            if not node: # base case if we are at the leaf
                return 0
            
            good = 1 if node.val >= max_so_far else 0 # is this node good?

            new_max = max(max_so_far, node.val) # updates running max
            
            good += dfs(node.left, new_max) # add counts of good nodes from left side
            good += dfs(node.right, new_max) # add counts of good nodes from right side
            
            return good # on the way up, good is summed up among
                        # all child nodes to get the total good nodes
        return dfs(root, root.val)