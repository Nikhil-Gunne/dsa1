class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def bfs(r,c):
            sm = 0
            q = deque([(r,c)])
            while q:
                currR,currC = q.popleft()
                if visited[currR][currC]:
                    continue
                visited[currR][currC] = True
                sm += grid[currR][currC]
                for x,y in directions:
                    dx = currR + x
                    dy = currC + y
                    if min(dx,dy) < 0 or dx == rows or dy == cols or visited[dx][dy]:
                        continue
                    elif grid[dx][dy]:
                        q.append((dx,dy))
            # print(sm)
            return sm
        
        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j]:
                    res = bfs(i,j)
                    if res % k == 0:
                        cnt += 1
        return cnt
                
        