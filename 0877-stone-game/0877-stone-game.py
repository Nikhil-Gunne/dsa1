class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def solve(s,e):
            if s>e:
                return 0
            
            if s==e:
                return piles[s]
            if (s,e) in dp:
                return dp[(s,e)]
            
            takesFromStart = piles[s] - solve(s+1,e)
            takesFromEnd = piles[e] - solve(s,e-1)
            dp[(s,e)] = max(takesFromStart,takesFromEnd)
            return dp[(s,e)]
        return solve(0,len(piles)-1) >= 0
