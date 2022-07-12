class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        appearences = {}
        for num in nums:
            if num not in appearences:
                appearences[num] = 0
            appearences[num] += 1
            
            if appearences[num] > (n/2):
                return num
        return -1