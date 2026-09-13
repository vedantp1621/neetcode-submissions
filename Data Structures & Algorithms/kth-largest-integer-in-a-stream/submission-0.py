class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k # create the vars, one list one int

        heapq.heapify(self.minHeap) # o(n) operation, reorder list in place to build
                                    # minheap

        while len(self.minHeap) > k: # trim the bottom elements so that we only have 
                                     # top k values 
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int: # when you add a value, make sure that it doesnt
                                    # cause the heap to exceed k values
                                    # since we have min heap, returning the top value
                                    # of the heap is the kth largets
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

        
        
        
