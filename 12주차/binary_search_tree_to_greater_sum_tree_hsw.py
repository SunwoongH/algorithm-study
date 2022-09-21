class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.num = 0
        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.right)
            temp = node.val
            node.val += self.num
            self.num += temp
            dfs(node.left)
        dfs(root)
        return root