class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        minPrice = int(1e9)

        for price in prices:
            minPrice = min(minPrice, price)
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)

        return maxProfit