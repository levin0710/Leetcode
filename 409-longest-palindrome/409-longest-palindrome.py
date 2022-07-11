class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = set()
        
        for letter in s:
            if letter in letters:
                letters.remove(letter)
            else:
                letters.add(letter)
                
        if len(letters) == 0:
            return len(s)
        return  len(s) - len(letters) + 1
            