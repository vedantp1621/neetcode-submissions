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
        oldToCopy = {None: None} # hash map to store copies of nodes. We will map
                                 # old nodes to the new copies

        cur = head # init the iterator to the head to start the first pass
                   # In the first pass: we will simply copy over the nodes from the
                   # old version to the new version
        while cur: # looping logic
            copy = Node(cur.val) # get the value of the node 
            oldToCopy[cur] = copy # create a new node with the same value
            cur = cur.next # looping logic
        cur = head # re init the iterator to the head to start the second pass
                   # In the second pass: we will set the pointers using the old nodes
                   # pointers
        while cur: # looping logic
            copy = oldToCopy[cur] # get the new node associated with the index
            copy.next = oldToCopy[cur.next] # set that nodes next value based on the next
                                            # chronological node in the hash map
            copy.random = oldToCopy[cur.random] # set that nodes random value based on the 
                                                # node present at the random index in the 
                                                # hash map (which is 0 indexed)
            cur = cur.next # looping logic
        return oldToCopy[head] # return the node at the head