# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Two Pointers.
#   One will go all the way to the end
#   Second will go all the way until it is n away from the end
#   Both pointers will keep track of how many times they iterated forward

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 0 -> head -> ... -> ... -> ... -> ...
        
        dummy = ListNode(0, head) # this dummy node is not shifted at all. It
                                  # is used to keep track of the entire chain
                                  # so that we can return at the end. The reason
                                  # the chain stays rooted to this is because
                                  # left is initialized as part of dummy. Once
                                  # left's next pointer is changed, those changes'
                                  # are reflected under the dummy's chain
        left = dummy # connect left to dummy to keep all changes rooted at dummy
        right = head # right will start one -> from left

        while n > 0: # in this loop, we are going to initialize the offset. 
                     # I.e: since we are removing the node that is n from
                     # the right, we can create that offset from the beginning
                     # and then shift both pointers all the way to the end. The
                     # left one will be used to remove the target
            right = right.next # shift until the gap is made
            n -= 1 # once this is 0, the gap is made

        while right: # shift both pointers ->. The left pointers next reference
                     # will be the one to remove
            left = left.next
            right = right.next

        left.next = left.next.next # skip the next reference, effectively deleting
                                   # it
        return dummy.next # return the head rooted at dummy