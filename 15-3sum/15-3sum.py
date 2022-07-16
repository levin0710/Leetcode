class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        triplets = set()
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            num = nums[i]
            
            while left < right:
                sumation = num + nums[left] + nums[right]
                array = [num, nums[left], nums[right]]
                if sumation == 0:
                    if array not in answer:
                        answer.append(array)
                    left += 1
                elif sumation < 0:
                    left += 1
                elif sumation > 0:
                    right -= 1
        return answer