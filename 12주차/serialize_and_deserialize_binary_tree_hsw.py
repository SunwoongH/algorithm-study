import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        encode = []
        def bfs(node):
            queue = collections.deque([node])
            while queue:
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    encode.append(str(node.val))
                else:
                    encode.append('.')
        bfs(root)
        return ' '.join(encode)

    def deserialize(self, data):
        if not data or data[0] == '.':
            return
        decode = data.split()
        root = TreeNode(int(decode[0]))
        def bfs(root: TreeNode, end: int) -> TreeNode:
            queue = collections.deque([root])
            i = 1
            while queue:
                node = queue.popleft()
                if i >= end:
                    break
                if decode[i] != '.':
                    node.left = TreeNode(int(decode[i]))
                    queue.append(node.left)
                i += 1
                if decode[i] != '.':
                    node.right = TreeNode(int(decode[i]))
                    queue.append(node.right)
                i += 1
            return root
        return bfs(root, len(data))