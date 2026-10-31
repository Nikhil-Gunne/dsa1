class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        mod = 10**9+7

        dp = [[-1] * cols for _ in range(rows)]
        def solve(r,c):
            if r == rows-1 and c==cols-1:
                return 1
            if  r == rows or c == cols:
                return 0 
            
            if dp[r][c] != -1:
                return dp[r][c]
            
            rC = c + 1
            right = 0
            down = 0
            dR = r + 1
            if rC < cols:
                currDir = 'R'
                dx = r
                dy = rC
                while  dx < rows and dy < cols and grid[dx][dy]:
                    if currDir == 'R':
                        dx += 1
                        currDir = 'D'
                    else:
                        dy += 1
                        currDir = 'R'
                right = solve(dx,dy)
            
            if dR < rows:
                currDir = 'D'
                dx = dR
                dy = c
                while  dx < rows and dy < cols and grid[dx][dy]:
                    if currDir == 'R':
                        dx += 1
                        currDir = 'D'
                    else:
                        dy += 1
                        currDir = 'R'
                down = solve(dx,dy)
            dp[r][c] = (right + down ) % mod
            return dp[r][c]
        return solve(0,0) % mod

            

        