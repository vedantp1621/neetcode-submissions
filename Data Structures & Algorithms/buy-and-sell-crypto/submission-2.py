class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # input an integer array
        # each elem in the list is anb integer value of the price of the coin
        # index is the day

        # goal is to choose a single day to buy, single to sell, and have optimal buy sell day

        # we need to track the max prift


        max_prof = 0
        left = 0
        
        # sliding iwndo approach, start both poiters at start

        for r in range(len(prices)):
            if prices[left] > prices[r]:
                left = r

            max_prof = max(max_prof, prices[r]-prices[left])

        return max_prof


