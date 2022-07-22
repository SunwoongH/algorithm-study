from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r: int, c: int, n: int, m: int) -> None:
            move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            queue = collections.deque([(r, c)])
            while queue:
                r, c = queue.popleft()
                for oper in move:
                    dr = r + oper[0]
                    dc = c + oper[1]
                    if dr >= 0 and dr < n and dc >= 0 and dc < m and grid[dr][dc] == '1':
                        grid[dr][dc] = '0'
                        queue.append((dr, dc))
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(i, j, len(grid), len(grid[0]))
                    count += 1
        return count