class Solution:
    longest: int = 0
    
    def diameterOfBinaryTree(self, root) -> int:

        def dfs(node) -> int:
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.longest = max(self.longest, left + right + 2)
            
            #상태값
            return max(left, right) + 1
        
        dfs(root)
        return self.longest