from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            num = 0
            num += dfs(node.left)
            num += dfs(node.right)
            return num + node.val if low <= node.val <= high else num
        return dfs(root)