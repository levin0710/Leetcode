class Solution:
    def climbStairs(self, n: int) -> int:
        waysToTop = [1 for i in range(n + 1)]
        
        for i in range (2, len(waysToTop)):
            waysToTop[i] = waysToTop[i-1] + waysToTop[i-2]
            
        return waysToTop[n]