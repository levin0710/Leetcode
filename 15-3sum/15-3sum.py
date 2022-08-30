class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
        
            while left < right:    
                if nums[i] + nums[left] + nums[right] == 0:
                    arr = [nums[i], nums[left], nums[right]]
                    if arr not in answer:
                         answer.append(arr)
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return answer
            