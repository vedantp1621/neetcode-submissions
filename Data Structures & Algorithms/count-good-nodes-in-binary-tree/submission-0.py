# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
# BFS

'''
somehow track the greatest node in a node's path


by recursing, we have the stack trace of the entire path trace to that node

base case
'''

class Solution:
    good_nodes = 0

    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root: TreeNode, prev_max):
            if root is None:
                return 0

            res = 1 if root.val >= prev_max else 0
            prev_max = max(root.val, prev_max)
            res += dfs(root.right, prev_max)
            res += dfs(root.left, prev_max)
            return res

        return dfs(root, root.val)
        







        