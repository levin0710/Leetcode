class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        
        for letter in s:
            if letter not in letters:
                letters[letter] = 0
            letters[letter] += 1
        
        for letter in t:
            if letter in letters:
                letters[letter] -= 1
            else:
                return False
            
            if letters[letter] == 0:
                letters.pop(letter)
        
        return len(letters) == 0