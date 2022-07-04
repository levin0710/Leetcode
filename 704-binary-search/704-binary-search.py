class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right)//2
            middleNum = nums[middle]
            
            if middleNum == target:
                return middle
            elif middleNum < target:
                left = middle + 1
            else:
                right = middle - 1
                
        return -1