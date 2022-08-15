from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.length = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            self.length = max(self.length, left_depth + right_depth)
            return max(left_depth, right_depth) + 1
        dfs(root)
        return self.length