# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# the structure of this problem is very common, memorize this pattern. outer func, global varibvale, 
# with inner function

# Realize: a normal DFS already accomplishes this, it goes all the way right until it cant anymore, 
# goes left
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = [] # global tracker

        def dfs(node, depth): # we will do a dfs with depth to figure out if we are at the lowest point
                              # in the tree
            if not node: # if this node is null, aka we went to far down 
                return None 
            if depth == len(res): # if this node is the lowest possible node
                res.append(node.val) # add it 
            # this stops any potential nodes being added when they are not the lowest 
            dfs(node.right, depth + 1) # keep searching, starting by going right
            dfs(node.left, depth + 1) # naturally, once the right side is done, the left side will trigger

        dfs(root, 0) # start the recursion
        return res # retrn

