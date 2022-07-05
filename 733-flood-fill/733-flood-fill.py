class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startingColor = image[sr][sc]
        queue = [[sr, sc]]
        visited = [[False for row in col] for col in image]
        
        while len(queue) > 0:
            currentSpot = queue.pop(0)
            row, col = currentSpot
            image[row][col] = color
            if visited[row][col]:
                continue
            
            visited[row][col] = True
            if row - 1 >= 0:
                if image[row - 1][col] == startingColor:
                    queue.append([row - 1, col])
            if col - 1 >= 0:
                if image[row][col - 1] == startingColor:
                    queue.append([row, col - 1])
            if row + 1 < len(image):
                if image[row + 1][col] == startingColor:
                    queue.append([row + 1, col])
            if col + 1 < len(image[sr]):
                if image[row][col + 1] == startingColor:
                    queue.append([row, col + 1])
        
        
    
        return image