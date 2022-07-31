from typing import List
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        visited = [False for _ in range(numCourses)]
        seen = set()
        def dfs(start: int) -> None:
            if start in seen:
                return False
            seen.add(start)
            is_cycle = False
            for u in graph[start]:
                if not visited[u]:
                    visited[u] = True
                    is_cycle = dfs(u) if not is_cycle else is_cycle
                    visited[u] = False
                else:
                    return True
            return is_cycle
        for u in range(numCourses):
            visited[u] = True
            if dfs(u):
                return False
            visited[u] = False
        return True