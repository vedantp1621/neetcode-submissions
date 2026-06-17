# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Uses floyd's tortoise and hare
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head # both pointers start at the same place

        while fast and fast.next: # fast is being checked here because it will
                                  # the first to reach a null pointer. The 
                                  # reason we have to check fast and fast.next is
                                  # because fast is moving two at a time. If the 
                                  # immediate neighbor or self is null, then we 
                                  # will run into an error, there wont be a 
                                  # fast.next.next

            fast = fast.next.next # move fast by 2
            slow = slow.next # move slow by 1

            if fast == slow: # in the case of a cycle, fast will ALWAYS catchup to
                             # slow, since they are moving in a circle
                return True # if fast does reach slow, that means that we found 
                            # a cycle

        return False # reaching this point means that no cycle was found and
                     # instead, fast found a null pointer