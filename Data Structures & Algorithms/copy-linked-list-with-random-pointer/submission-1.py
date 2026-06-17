"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # given the head and length of a linked list
        # each node has the next ptr, and a random ptr to a random node in the list (or null)
        # create a deep copy (for eah node, orig val, next ptr to a new node corr to the next 
        #    ptr of the old node, same w random)
        # no ptrs in new list should point to nodes in orig list
        # retyrn head of copied list
        
        '''
        Need two traversals
        first traverse: get all the indexes for each node and store then 
            maybe store in dict where index:object
        second traversal: iterate through orig linkedlist: use the next and random ptr index values
                                                           to retrieve the object details from the hash
        '''
        oldToCopy = {None: None}

        # first traversal create the link:
        curr = head
        while curr:        
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            oldToCopy[curr].next = oldToCopy.get(curr.next)
            oldToCopy[curr].random = oldToCopy.get(curr.random)
            curr = curr.next
        return oldToCopy[head]







