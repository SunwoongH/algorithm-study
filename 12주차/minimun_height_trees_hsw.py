from typing import List
import collections

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        count = n
        curr_leaf = []
        for u in graph:
            if len(graph[u]) == 1:
                curr_leaf.append(u)
        while count > 2:
            next_leaf = []
            for child in curr_leaf:
                parent = graph[child].pop()
                graph[parent].remove(child)
                if len(graph[parent]) == 1:
                    next_leaf.append(parent)
            count -= len(curr_leaf)
            curr_leaf = next_leaf
        return curr_leaf if n > 1 else [0]