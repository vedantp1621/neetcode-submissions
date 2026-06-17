# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# This is essentially a reskin of the calculate # of nodes problem, or total value of tree problem
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        def dfs(root: TreeNode, prev_max): # recursive DFS function that will iterate down the tree to each node
            if root is None: # base case, we have reached the bottom/null node and dont want to consider it
                return 0

            res = 1 if root.val >= prev_max else 0 # if the condition for this node is valid, we add it to the 
                                                   # total, otherwise, dont add anuthing
            prev_max = max(root.val, prev_max) # change the previous maximum
            res += dfs(root.right, prev_max) # add the right subtrees valid nodes
            res += dfs(root.left, prev_max) # add the left subtrees valid nodes
            return res # return this subtrees acummulation

        return dfs(root, root.val) # return entire tree acumulation
        







        