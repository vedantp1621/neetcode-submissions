# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#IMPORTANT PROBLEM, DO A TRAVERSAL OF THIS TO UNDERSTAND
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # how do we know that then child to the left is less than the parent and the same with the right

        def dfs(minval, maxval, curr_node):
            if not curr_node: return True

            if not (minval < curr_node.val < maxval): return False

            return dfs(curr_node.val, maxval, curr_node.right) and dfs(
                minval, curr_node.val, curr_node.left)

        return dfs(float("-inf"), float("inf"), root)


        

        
        