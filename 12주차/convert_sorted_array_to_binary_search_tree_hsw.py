from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def implementation_bst(left: int, right: int) -> TreeNode:
            if left > right:
                return
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = implementation_bst(left, mid - 1)
            node.right = implementation_bst(mid + 1, right)
            return node
        return implementation_bst(0, len(nums) - 1)