class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = prices[0]
        
        for num in prices:
            minPrice = min(minPrice, num)
            profit = max(profit, num - minPrice)
        return profit
        