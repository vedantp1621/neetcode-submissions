"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# we have some node definition, storing the value of a specific node and a node list of all the neighbors

# a deep copy is one where the copy is it's own entity with the exact same values and neighbors of the original 

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    
    # Use a hashmap mapping each original node to its cloned node.
    # Starting from the input node, traverse the graph using DFS/BFS.
    # For every node we encounter:
    #   - create a clone if one doesn't already exist
    #   - traverse its neighbors
    #   - connect the cloned node to the cloned versions of its neighbors
    # The hashmap prevents infinite loops caused by cycles.


        # gate to check trivial input
        if not node:
            return None

        # create a dict to store links between orig and clone
        # doubles as a way to track if the node has a clone created
        clone_mapping = {}

        # init by creating a clone of the input node

        # add this node to the queue. nodes in queue are rpocessed like this
        # 1. popped
        # 2. neighbors are checked to see if they have copies. 
        # 3. if not, create a copy for that neighbor and add it to the queue to
        #    be processed later
        # 4. append the neighbor copy to the visiting nodes clone neighbors list

        # basic idea is that we need to create the clones first for neighbors as we discover them, then populate the visiting node's neighbors list

        clone_mapping[node] = Node(node.val) 
        q = deque([node]) 

        while q:
            visiting_node = q.popleft()
            neighbors = visiting_node.neighbors

            for neighbor in neighbors:
                if neighbor not in clone_mapping: # if the neighbor doesnt have a clone, create a clone
                    clone_mapping[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                clone_mapping[visiting_node].neighbors.append(clone_mapping[neighbor])

        return clone_mapping[node]
            
                


            






        


        