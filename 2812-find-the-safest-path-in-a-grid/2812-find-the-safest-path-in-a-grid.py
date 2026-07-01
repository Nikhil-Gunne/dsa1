import heapq
from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] or grid[rows-1][cols-1]:
            return 0

        thieves = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    grid[r][c] = 0  
                    thieves.append((r, c))
                else:
                    grid[r][c] = -1  

        while thieves:
            curr = len(thieves)
            for _ in range(curr):
                r, c = thieves.popleft()
                for x, y in [(0,1),(0,-1),(1,0),(-1,0)]:
                    dx, dy = r + x, c + y
                    if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == -1:
                        grid[dx][dy] = grid[r][c] + 1
                        thieves.append((dx, dy))

        visited = set()
        heap = [(-grid[0][0], 0, 0)]
        while heap:
            safe, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == rows - 1 and c == cols - 1:
                return -safe
            for x, y in [(0,1),(0,-1),(1,0),(-1,0)]:
                dx, dy = r + x, c + y
                if 0 <= dx < rows and 0 <= dy < cols and (dx, dy) not in visited:
                    newSafe = min(-safe, grid[dx][dy])
                    heapq.heappush(heap, (-newSafe, dx, dy))
        return 0