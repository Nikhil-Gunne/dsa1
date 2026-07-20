class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        rows = len(grid)
        cols = len(grid[0])

        temp = []

        for i in range(rows):
            for j in range(cols):
                temp.append(grid[i][j])

        n = len(temp)
        k %= n

        def rev(s, e):
            while s < e:
                temp[s], temp[e] = temp[e], temp[s]
                s += 1
                e -= 1

        rev(0, n - 1)
        rev(0, k - 1)
        rev(k, n - 1)

        idx = 0
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = temp[idx]
                idx += 1

        return grid