class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashmap = {}
        
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1
            
        
        for key in hashmap:
            if hashmap[key] % 2 != 0:
                return False
        return True
        