class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # array of stones where each stone is the ith stones weight

        # we want to run a sim:
        # each step -> choose two heaviest stones with weight x and y
        # if x == y, both stones are destroyed
        # if x < y, the x stone is destroyed and y has y-x weight
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first_rock = heapq.heappop(stones)
            second_rock = heapq.heappop(stones)

            if second_rock > first_rock:
                heapq.heappush(stones, first_rock-second_rock)

        stones.append(0)
        return abs(stones[0])

        


        