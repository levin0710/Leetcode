class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = [1 for num in nums]
        
        for i in range(1, len(nums)):
            answer[i] = nums[i - 1] * answer[i-1]
        
        multiplier = 1
        
        for i in reversed(range(len(nums))):
            answer[i] *= multiplier
            multiplier *= nums[i]
        return answer