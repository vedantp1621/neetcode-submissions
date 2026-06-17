class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # we're going to use two pointers. the left pointer will be the 'buy'
                    # point, and the right pointer will be the 'sell' point
        maxP = 0 # we will keep track of the highest profit margin

        while r < len(prices): # once the right pointer reaches the end, that means we 
                               # considered every 'sell' point, and can now end the search
            if prices[l] < prices[r]: # checks if l is less than r. meaning theres a profit
                profit = prices[r] - prices[l] # calculate the profit
                maxP = max(maxP, profit) # if the new profit is better than previous, replace
                                         # it
            else: # otherwise, the l pointer is higher than the r, meaning we found a new low
                  # buying point, set l to r
                l = r
            r += 1 # at the end of each check, we iterate r forward to keep the loop running
        return maxP # the final 'best profit' that was set will be the one thats returned