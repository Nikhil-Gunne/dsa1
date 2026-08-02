class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        total = sum(piles)
        n = len(piles)
        dp = [[-1]*n for _ in range(n)]
        def pick(start,end):

            if start>end:
                return 0
            if dp[start][end] != -1:
                return dp[start][end]
            
            fs = piles[start] + max(pick(start+2,end),pick(start+1,end-1))
            fe = piles[end] +  max(pick(start,end-1),pick(start+1,end-1))
            dp[start][end] = max(fs,fe)
            return dp[start][end]
        res = pick(0,len(piles)-1)
        
        if res >total//2:
            return True
        return False


        