# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = [] # list to track sublists

        def dfs(node, depth): # 
            if not node: # Base case: node is null, so we cut this instance
                return
            if depth == len(levels): # Case where we find a new level, in
                                     # which case we need to create a new
                                     # sublist in levels
                levels.append([])   # new level
            levels[depth].append(node.val) # we do a DFS, but add the node
                                           # to the specific level in levels
                                           # I.e, we are not adding level by 
                                           # level, we are populating sublist
                                           # 1, then 2, then 3, then back to 1
                                           # then 2, then 3, ...
            dfs(node.left, depth + 1) # basic DFS recurse statements
            dfs(node.right, depth + 1)

        dfs(root, 0) # initialize the function call stack
        return levels # return the final sublist

        