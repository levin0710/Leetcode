class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashset = set()
        
        for letter in s:
            if letter not in hashset:
                hashset.add(letter)
            else:
                hashset.remove(letter)
        
        if len(hashset) == 0:
            return len(s)
        
        return len(s) - len(hashset) + 1