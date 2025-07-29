class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy and hold
        # sell
        if len(prices) == 1:
            return 0

        max_profit = float('-inf')
        min_price = float('inf')
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            max_profit = max(prices[i] - min_price, max_profit)
        
        return max_profit