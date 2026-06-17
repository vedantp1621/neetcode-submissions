# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # we use a dummy node to track the final list, since we 
                           # want to return a linked list
        cur = dummy

        carry = 0 # this carry variable will be used to store the 1 when numbers like 5 and 8
                  # are added. By having a carry variable, we can continue the loop to account 
                  # for the extra iteration in one of the lists
        while l1 or l2 or carry: # as long as there is a list that has a digit, we must continue
                                 # accounting for digits 

            v1 = l1.val if l1 else 0 # init variables to use for addition
            v2 = l2.val if l2 else 0 # init variables to use for addition
                                     # by making the else 0, we account for edge cases where one
                                     # list has a greater amount of digits vs the other

            # new digit: performes the logic of addition: adding by digit and carrying over when
            # neccessary
            val = v1 + v2 + carry  
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val) # set the next node of the new list to the value 

            # update pointers (iterate forward)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next # return the original dummy pointer that tracks the new list