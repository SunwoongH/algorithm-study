from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            new_node = TreeNode()
            new_node.val = node.val
            new_node.right = dfs(node.left)
            new_node.left = dfs(node.right)
            return new_node
        return dfs(root)