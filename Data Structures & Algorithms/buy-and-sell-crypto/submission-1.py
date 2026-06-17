class Solution:
    def maxProfit(self, prices: List[int]) -> int:

# array of integers representing a price of a coin
# must choose a two points, first to buy second to sell

# use two pointers,
# if first pointer greater than second pointer, push first
# if two pters same, push second 

# keep pushing second and marking max profit 

        buy, sell = 0, 1
        max_profit = 0

        
        while sell < len(prices):
            if prices[buy] < prices[sell]: # good time to buy 
                profit = prices[sell] - prices[buy]
                max_profit = max(profit, max_profit)
            else: # buy more expensive than sell
                buy = sell
            sell += 1
        return max_profit

            
        