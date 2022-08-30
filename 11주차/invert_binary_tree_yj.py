import collections

def invertTree(self, root):
  queue = collections.deque([root])
        
  while queue:
    node = queue.popleft()
            
    #부모 노드부터 하향식 스왑
    if node:
      node.left, node.right = node.right, node.left
                
      queue.append(node.left)
      queue.append(node.right)
      
  return root