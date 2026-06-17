# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, current = None, head # initialize the pointers, we need to link all
                                   # linear directions
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6

        while current: # once current is not pointin to anything we stop
            temp = current.next # we need to have a temp keep track of the original
                                # sequence because we are messing around with the next
                                # pointer
            current.next = prev # flip the next pointer to the last iterations 'current'
                                # aka, prev

            prev = current # have the prev point to the current iteration, so when we 
                           # visit the next node, that node's next becomes the previous
            current = temp # iterate the current node to the next, natural looping for 
                           # linked lists
            
        return prev # prev has the linking

