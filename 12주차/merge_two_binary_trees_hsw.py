from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node_1, node_2):
            if not node_1 and not node_2:
                return
            node = TreeNode()
            if node_1:
                node.val += node_1.val
            if node_2:
                node.val += node_2.val
            node.left = dfs(node_1.left if node_1 else None, node_2.left if node_2 else None)
            node.right = dfs(node_1.right if node_1 else None, node_2.right if node_2 else None)
            return node
        return dfs(root1, root2)