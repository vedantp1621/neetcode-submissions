# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:   
   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # clean the data, if the root we're at is null, this iter is false
        # if the subroot is null, it means that we can return True, since the only way that 
        # we find a null subroot is if we had an equivalent node, and had to iterate down
        if not subRoot:
            return True
        if not root:
            return False

        # chcek this combination of root and subroot. the same tree function bascially iterates down
        # the subtree and its counterpart in the main tree. it checks each node and fully returns 
        # True once each node has been checked and have been found equal
        if self.sameTree(root, subRoot):
            return True
        # othewise, if above was not valid, we can itearte down the main tree and start the subtree
        # check again
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # this func checks each node in the subtree with its counterpart in the root. if boht
        # trees iterated as far to find null nodes, that means that we have not found a unewqyal
        # pairing. if there is unequal pairing, the return False would have been triggered
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                   self.sameTree(root.right, subRoot.right))
        return False

