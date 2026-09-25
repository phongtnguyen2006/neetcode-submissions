class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        each pos either buy, sell, or skip
        """
        
        min_price = float('inf')
        profit = 0

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            print(prices[i], min_price)
            if prices[i] - min_price > 0:
                profit += prices[i] - min_price
                min_price = prices[i]

        return profit
