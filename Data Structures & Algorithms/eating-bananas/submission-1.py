import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # array of ints, each being the # of bananas per i pile
        # integer h, # hours you have to eat all bananas
        # return minimum banana per hour eating rate 
        # - each hour you choose one pile only
        # - if you finish early, you cannot move

        '''
        how to check if you can eat all bananas (each step) -> 0(n)
        - iterate through each pile, check if bpm >= i pile size
        - if yes, +1 hours and go to next pile
        - if no, + pile size/bpm (use math.ceil)

        brute force, enumerate starting at 1 bpm and check if you can eat all piles,
        keep adding 1 and checking. this would be O(n) outer loop

        optimize, do binary search on the outer loop to make it O(logn) outer
        '''

        #at each step
        def checkbpm(k: int) -> bool:
            hours = 0

            for pile in piles:
                if k >= pile:
                    hours += 1
                else:
                    hours += math.ceil(pile/k)
                
                if hours > h:
                    return False
            
            return True

        l,r = 1, max(piles)

        while l < r:
            m = l + (r-l) // 2

            if checkbpm(m): # means that the limit could be lessened
                r = m
            else:
                l = m + 1
        return l


1, 2, 3, 4, 5, 6, 7
                

        

         





