class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        for i in range(n):
            intervals[i].append(i)
        
        intervals.sort()
        # print(intervals)
        def binarySearch(tar):
            low = 0
            high = n-1
            res = n
            while low <= high:
                mid = low + (high-low)//2
                
                if intervals[mid][0] > tar:
                    res = mid
                    high = mid - 1 
                else:
                    low = mid + 1
            return res 
        nextIdx = [n] * n
        for i in range(n):
            nextIdx[i] = binarySearch(intervals[i][1])
        
        class Node:
            def __init__(self):
                self.score = 0
                self.idxs = []
        
        dp = [[-1] *(5) for _ in range(n+1)]
        def solve(idx,k):
            if k == 0  or idx == n:
                return Node()
            
            if dp[idx][k] != -1:
                return dp[idx][k]

            skip = solve(idx+1,k)
            nextNode = solve(nextIdx[idx],k-1)
            take = Node()
            take.score = nextNode.score + intervals[idx][2]
            take.idxs = nextNode.idxs.copy()
            take.idxs.append(intervals[idx][3])
            take.idxs.sort()

            if skip.score > take.score:
                dp[idx][k] = skip
                return skip
            elif take.score > skip.score:
                dp[idx][k] = take
                return take
            else:
                dp[idx][k] = skip if skip.idxs < take.idxs else take
                return dp[idx][k]
            
        return solve(0,4).idxs

        




        