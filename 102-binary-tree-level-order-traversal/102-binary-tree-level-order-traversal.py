# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        answer = []
        
        queue = [root]
        
        while queue:
            internalQueue = []
            level = []
            for tree in queue:
                if tree is not None:
                    level.append(tree.val)
                    internalQueue.append(tree.left)
                    internalQueue.append(tree.right)
            if len(level) > 0:
                answer.append(level)
            queue = internalQueue
        return answer