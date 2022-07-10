# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        middle = 1
        while left <= right:
            middle = (left + right) // 2
            
            if isBadVersion(middle):
                if isBadVersion(middle + 1) and not isBadVersion(middle - 1):
                    return middle
                right = middle - 1
            else:
                left = middle + 1
        return middle