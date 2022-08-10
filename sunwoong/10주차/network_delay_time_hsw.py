import sys
import collections
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, time in times:
            graph[u].append((v, time))
        def dijkstra(start: int) -> List[int]:
            delay = [sys.maxsize for _ in range(n + 1)]
            delay[start] = 0
            heap = [(0, start)]
            while heap:
                time, u = heapq.heappop(heap)
                if delay[u] < time:
                    continue
                for adj_v, adj_time in graph[u]:
                    if delay[adj_v] > time + adj_time:
                        delay[adj_v] = time + adj_time
                        heapq.heappush(heap, (delay[adj_v], adj_v))
            return delay
        time = 0
        delay = dijkstra(k)
        for u in range(1, n + 1):
            if delay[u] == sys.maxsize:
                return -1
            time = max(time, delay[u])
        return time