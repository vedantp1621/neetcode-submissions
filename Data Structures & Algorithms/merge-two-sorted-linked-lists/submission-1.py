# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        top_pointer = merged = ListNode() # Key Technique: top_pointer will always point to
                                          # first node in the chain. To add to the chain, all
                                          # you need to do is use merged.next to link a new 
                                          # node. Then, you can iterate down using merged = merged.next
                                          # I.e merged will keep going down and top_pointer will stay

        while list1 and list2: # Loop handles cases when you have to choose a list to add over
                               # another, aka when both are non-null
            if list1.val < list2.val: # list1 < list2
                merged.next = list1 # set the next node to the list1 top node
                list1 = list1.next # iterate the list1 to the next
            else: # list2 < list1
                merged.next = list2 # set the next node to the list2 top node
                list2 = list2.next # iterate the list2 to the next
            
            merged = merged.next # now, since we handled the additions in this round, we
                                 # can iterate the merged pointer to the newly added node

        merged.next = list1 or list2 # This handles cases when one list1 or list2 is null.
                                     # Using the or in this way automatically adds the rest
                                     # of the non-null list. Since we add the pointer to the
                                     # rest of the list to merged, we are now done, the entire 
                                     # remainder has been added

        return top_pointer.next # return the .next since the first value is a placeholder