class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        x = 0
        y = len(mat) - 1
        
        finalSum = 0
         
        while x < len(mat):
            if x == y:
                finalSum += mat[x][x]
                x += 1
                y -= 1
                continue
            finalSum += mat[x][x]   
            finalSum += mat[x][y]
            x += 1
            y -= 1
        return finalSum
            