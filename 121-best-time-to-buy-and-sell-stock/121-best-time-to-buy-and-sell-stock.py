class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProf = 0
        
        for i in range(len(prices)):
            price = prices[i]
            maxProf = max(price - minPrice, maxProf)
            minPrice = min(price, minPrice)
        return maxProf