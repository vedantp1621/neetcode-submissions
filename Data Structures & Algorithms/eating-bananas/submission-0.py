class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # in essence, this is a binary problem. We start with a far left bound and a far right
        # bound. left is the slowest rate, right is the fastest rate
        left, right = 1, max(piles) # 1 banana per hour is slowest, and the fastest is whichever
                                    # number would make it 1 pile per min, I.e. the max
        result = right # this stores the most suitable speed found, starting at the fastest

        while left <= right:
            middle = (right+left)//2  # typical middle pointer algo, finds the midpoint
                                      # between the two ends
            # trickiest part of problem: this is the backend processing that calculates the 
            # time it would take, in hours, to eat the bananas for each speed middle
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / middle)

            # now, we compare our target hours to the middle hours, allowing us to see if we 
            # need to speed up left or slow down right
            if h < totalTime: # what this is checking: we need faster speeds, the ones we
                              # are checking are too slow
                left = middle + 1
            else: # what this is checking: we are going to check slower speeds to see if 
                  # the monkey can lower its eating rate and still get by. For now, this is
                  # the best rate
                result = middle
                right = middle - 1
        return result
    
      