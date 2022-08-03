# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], largerThan=float("-inf"), lessThan=float("inf")) -> bool:
        
        if root is None:
            return True
        elif root.val <= largerThan or root.val >= lessThan:
            return False
        
        return self.isValidBST(root.left, largerThan, min(lessThan, root.val)) and self.isValidBST(root.right, max(largerThan, root.val), lessThan)