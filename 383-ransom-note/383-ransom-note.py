class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterCount = {}
        
        if len(ransomNote) > len(magazine):
            return False
        
        for letter in magazine:
            if letter not in letterCount:
                letterCount[letter] = 0
            letterCount[letter] += 1
            
        for letter in ransomNote:
            if letter not in letterCount:
                return False
            letterCount[letter] -= 1
            if letterCount[letter] == 0:
                letterCount.pop(letter)
        return True
    