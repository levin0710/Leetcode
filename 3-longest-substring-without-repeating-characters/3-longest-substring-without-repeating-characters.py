class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        
        maxL = 0
        lettersSeen = set()
        
        start = 0
        end = 0
        
        while end < len(s):
            if start == end or s[end] not in lettersSeen:
                lettersSeen.add(s[end])
                end += 1
            else:
                maxL = max(maxL, len(s[start: end]))
                lettersSeen.remove(s[start]) 
                start += 1 
                
            
        maxL = max(maxL, len(s[start: end]))
        return maxL