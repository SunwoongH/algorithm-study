import collections

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
           
def maxDepth(self,root: TreeNode):
  if root is None:
    return 0
  queue = collections.deque([root])
  depth = 0
  
  while queue:
    depth +=1
    for _ in range(len(queue)):
      cur_root = queue.popleft()
      if cur_root.left:
        queue.append(cur_root.left)
      if cur_root.right:
        queue.append(cur_root.right)
        
  return depth
root = [3, 9, 20, None, None, 15,7]

maxDepth(root)# ??