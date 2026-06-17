# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1) First thing we want to do is find the middle point of the list.
        #   We will use fast, slow pointers to do this. 
        slow, fast = head, head.next

        while fast and fast.next: # this loop structure is common for linked lists
                                  # essentially loops until fast reaches the end
            slow = slow.next # slow moves by 1
            fast = fast.next.next # fast moves by 2

        #2) Now, we will reverse the second half of the list. The reason we do
        #   this is because the pattern: [0, n-1, 1, n-2, 2, n-3, ...], where
        #   we are inserting in -> direction starting from head and <- direction
        #   starting from tail. Reversing the pointers of the second half will
        #   allow us to move <-

        second = slow.next # the start of the second half is always the next
                           # of where the slow ended off
        slow.next = None # we want the last element of the first half to end 
                         # with a Null pointer so that we know when to stop,
                         # and so that the two halves get split
        prev = None # we want the first element in the second half to have
                    # its previous point to Null so that we know when to stop.
                    # Just like other linked list problems, we are using prev
                    # to track <- side nodes
        while second: # here we reverse the list until we reach the end. This algo
                      # is cruical and common, must understand
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #3) Now, we will work through merging the two halves into one. We will
        #   use two pointers, one on the far left moving -> and one on the far
        #   right moving <-. Process:
        #   a) insert left pointer node 
        #   b) insert right pointer node by setting left's next to right pointer
        #   c) set new right pointer's next to left's previous next
        #   d) move right pointer <-
        #   e) move left pointer ->
        #   f) stop once Null is reached

        second = prev # once the above list is done, second will be set to null
                      # so to start at the end and move <-, we must set it back
                      # to the last element
        first = head # start left pointer at head
        while second: # because of the way we split the halves, second half can
                      # be shorter, so to prevent errors we will stop when
                      # second reaches Null
            temp_first, temp_second = first.next, second.next # store the temp
                                                              # next nodes, so
                                                              # that we can 
                                                              # iterate <-,-> 
                                                              # even after changing
                                                              # nodes around               
            first.next = second # insert right side
            second.next = temp_first # set next pointer of new right side node
            first, second = temp_first, temp_second # move -> or <-















