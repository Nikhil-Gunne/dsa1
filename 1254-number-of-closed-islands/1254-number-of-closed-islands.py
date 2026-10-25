class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False

            if grid[r][c] == 1 or visited[r][c]:
                return True

            visited[r][c] = True

            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)

            return left and right and up and down

        cnt = 0

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if not visited[i][j] and grid[i][j] == 0:
                    if dfs(i, j):
                        cnt += 1

        return cnt