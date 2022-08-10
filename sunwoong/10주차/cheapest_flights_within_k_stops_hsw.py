import collections
import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, cost in flights:
            graph[u].append((v, cost))
        def dijkstra(start: int, end: int, k: int) -> int:
            visited = [0 for _ in range(n)]
            heap = [(0, start, -1)]
            while heap:
                cost, u, count = heapq.heappop(heap)
                if u == end:
                    return cost
                if count < k and (not visited[u] or visited[u] > count):
                    visited[u] = count
                    for adj_v, adj_cost in graph[u]:
                        heapq.heappush(heap, (cost + adj_cost, adj_v, count + 1))
            return -1
        return dijkstra(src, dst, k)