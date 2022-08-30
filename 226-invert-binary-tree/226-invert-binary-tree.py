# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tree = root 
        
        if tree is not None:
            tree.left, tree.right = tree.right, tree.left
            self.invertTree(tree.left)
            self.invertTree(tree.right)
        return root