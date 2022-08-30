from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for u, v in tickets:
            graph[u].append(v)
        for u in graph:
            graph[u].sort(reverse=True)
        result = collections.deque()
        def dfs(curr: str) -> None:
            while graph[curr]:
                next = graph[curr].pop()
                dfs(next)
            result.appendleft(curr)
        dfs('JFK')
        return result