# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], acc = 0) -> int:
        if root is None:
            return acc
        
        return max(self.maxDepth(root.left, acc + 1), self.maxDepth(root.right, acc + 1))