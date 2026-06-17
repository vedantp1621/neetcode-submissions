# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # two pters, one to list1 and one to list 2

        # if top pter is less <= bottom, add top current and iterate forwarc
        # otherwise, add bottom current and iterate forward

        l1_curr = list1
        l2_curr = list2


        dummy = res = ListNode()
        while l1_curr and l2_curr:
      
            if l1_curr.val < l2_curr.val:
                res.next = l1_curr
                l1_curr = l1_curr.next
            else:
                res.next = l2_curr
                l2_curr = l2_curr.next

            res = res.next

        res.next = l1_curr or l2_curr

        return dummy.next
