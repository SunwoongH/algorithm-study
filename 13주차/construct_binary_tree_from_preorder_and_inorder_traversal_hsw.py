from typing import List, Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_table = dict()
        for i, item in enumerate(inorder):
            inorder_table[item] = i
        preorder = collections.deque(preorder)
        def make_tree(left, right):
            if left > right:
                return
            value = preorder.popleft()
            pivot = inorder_table[value]
            node = TreeNode(value)
            node.left = make_tree(left, pivot - 1)
            node.right = make_tree(pivot + 1, right)
            return node
        return make_tree(0, len(inorder) - 1)