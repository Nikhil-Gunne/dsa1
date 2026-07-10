class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:

        pairs = [(nums[i],i) for i in range(n)]
        pairs.sort()
        # stores position of the node in sorted array
        nodePos = [0] * n 
        for i in range(n):
            nodePos[pairs[i][1]] = i
        
        farthestPoss = [[0]*int(log2(n)+1) for _ in range(n)]

        def binarySearch(i,tar):
            left = i
            right = n-1
            res = 0
            while left<=right:
                mid = left + ((right-left)//2)
                if pairs[mid][0] <= tar:
                    res = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return res

        for i in range(n):
            farthestPoss[i][0] = binarySearch(i,pairs[i][0]+maxDiff)
        
        jumps = int(log2(n))+1

        # binary lifting and storing farthest possible
        for j in range(1,jumps):
            for node in range(n):
                farthestPoss[node][j] = farthestPoss[farthestPoss[node][j-1]][j-1]

        res = []
        for u,v in queries:
            # get postion insorted array
            a = nodePos[u]
            b = nodePos[v]

            if a==b:
                res.append(0)
                continue
            
            if a>b:
                a,b = b,a
            
            curr = a
            jump = 0
            for j in range(jumps-1,-1,-1):
                if farthestPoss[curr][j] < b:
                    curr = farthestPoss[curr][j]
                    jump += (1<<j) 
            
            if farthestPoss[curr][0] >= b:
                res.append(jump+1)
            else:
                res.append(-1)


        return res
        