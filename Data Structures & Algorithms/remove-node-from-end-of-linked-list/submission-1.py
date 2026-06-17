# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # given the head of a linked list
        # we want to remove the nth node and return the head again

        # traversing to the nth node -> 0(n)
        # once we're there, we store the prev node
        # set prev.next.next to the next node
        dummy = ListNode(0, head)
        left, right = dummy, head

        if head.next == None:
            right = head

        for i in range (n):
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next



        
        # while node:  
        #     if iterator == n:
        #         if prev_node == None:
        #             return head.next
        #         prev_node.next = next_node
        #         break
            
        #     iterator += 1
        #     next_node = node.next
        #     prev_node = node
        
        # return root