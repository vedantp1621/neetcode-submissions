# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    
        if not p and not q: # means both have a null child that we are at
                            # we dont have to check value
            return True

        if p and q and p.val == q.val: # ensures both are non-null and have the same value, then we
                                       # can recurse downwards
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) # naturally recurses left and
                                                                      # right for us. if any of these
                                                                      # functions reutnr false, this will also be false                                                      # check wont succeed. 
            
        
        else: # othewise, the values did not match or one is null while the other isnt, so we return 
              # false
            return False