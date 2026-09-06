class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        sLen = len(s)
        tLen = len(t)

        dp = [[-1] * tLen for _ in range(sLen)]
        def solve(idx1,idx2):

            if idx1 == sLen or idx2==tLen:
                return 1 if idx2 == tLen else 0
            
            if dp[idx1][idx2] != -1:
                return dp[idx1][idx2]
            
            take = 0
            if s[idx1] == t[idx2]:
                take = solve(idx1+1,idx2+1)
            skip = solve(idx1+1,idx2)
            dp[idx1][idx2] =  take+skip
            return dp[idx1][idx2]
        return solve(0,0)
            

            
        