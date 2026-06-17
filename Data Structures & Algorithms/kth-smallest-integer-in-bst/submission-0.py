# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#DFS -> stack

# Go all the way down the left and then return until the k value is satisfied

# i # of times we have hit the recurse

# we go all the way down first
# we need a way to figure out when were coming back up
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k # doesnt change, so we dont pass it in everytime. just leave it nonlocal
        res = root.val

        def dfs(node):
            nonlocal cnt, res
            if not node: # typical dfs base case
                return
            # skeleton: left middle right is the natural least to greatest transition
            dfs(node.left) # start by going left
            cnt -= 1 # tracker to see how many times we have recursed upwards
            if cnt == 0: # if the tracker reaches 0, we went back up the stack
                         # enough times to find the final solutiom
                res = node.val # the final result is the node that we want
                return # return
            # as soon as the cnt is 0, we stop the chain and return until the stack is done
            dfs(node.right) # recurse right to keep natural order

        dfs(root) # start the stack
        return res # return finla res value
            