# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # put the nodes in buckets
        # at each level: add child nodes to a queue
        # add this node to a list
        # iterate through the queue?

        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            lev = []
            for _ in range(len(queue)):
                curr_node = queue.popleft() # now we have this node
                lev.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                     queue.append(curr_node.right)
            res.append(lev)
        return res
                







