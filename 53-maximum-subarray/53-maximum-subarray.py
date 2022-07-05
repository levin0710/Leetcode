class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largestSum =  float("-inf")
        currentLargest = float("-inf")
        for num in nums:
            currentLargest = max(num, currentLargest + num)
            largestSum = max(largestSum, currentLargest)
            
        return largestSum
        