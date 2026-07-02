class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        minHeap = [(grid[0][0],0,0)]
        visited = set()
        visited.add((0,0))
        rows = len(grid)
        cols = len(grid[0])
        while minHeap:
            currHealth,r,c = heappop(minHeap)
            if r==rows-1 and c==cols-1:
                # print(currHealth)
                return currHealth<health
            
            for x,y in [(0,1),(1,0),(0,-1),(-1,0)]:
                dx = r+x
                dy = c + y
                if min(dx,dy) >= 0 and dx < rows and dy < cols and (dx,dy) not in visited:
                    if currHealth + grid[dx][dy] < health:
                        visited.add((dx,dy))
                        heappush(minHeap,(currHealth + grid[dx][dy],dx,dy))
        return False
        