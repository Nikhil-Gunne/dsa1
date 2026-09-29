class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        dp = {}
        def solve(r,c,cnt):
            if cnt < 0:
                return False
            if r == rows-1 and c == cols-1:
                return True if cnt == 1 and grid[r][c] == ')' else False
            if r == rows or c == cols:
                return False
            if (r,c,cnt) in dp:
                return dp[(r,c,cnt)]
            right = solve(r,c+1,cnt + (-1 if grid[r][c]==')' else 1))
            down = solve(r+1,c,cnt + (-1 if grid[r][c]==')' else 1))
            dp[(r,c,cnt)] = right or down
            return dp[(r,c,cnt)]
        return solve(0,0,0)
            

            






        