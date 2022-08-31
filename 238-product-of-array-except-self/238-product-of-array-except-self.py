class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = [1 for num in nums]
        
        multiplier = 1
        
        for i in range(len(nums)):
            answer[i] *= multiplier
            multiplier *= nums[i]
            
        multiplier = 1
        
        for i in reversed(range(len(nums))):
            answer[i] *= multiplier
            multiplier *= nums[i]
            
        return answer