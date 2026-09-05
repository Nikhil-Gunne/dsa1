class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
       
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1
        
        visited = set()
        q = deque()
        q.append((0,0,0))
        visited.add((0,0))
        directions = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
        while q:
            steps,r,c = q.popleft()

            if r == rows - 1 and c== cols-1:
                return steps+1
            
            
            for x,y in directions:
                dx = r + x
                dy = c + y
                
                if min(dx,dy) < 0  or dx == rows or dy == cols or (dx,dy) in visited or grid[dx][dy] == 1:
                    continue
                
                q.append((steps +1 , dx,dy))
                visited.add((dx,dy))
        
        return -1
            