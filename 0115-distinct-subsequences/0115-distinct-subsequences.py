class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # memoization or top-down approach
        # T.C:O(N*M)
        # S.C:O(N*M) + O(N+M) for recursion stack

        sLen = len(s)
        tLen = len(t)

        # dp = [[-1] * tLen for _ in range(sLen)]
        # def solve(idx1,idx2):

        #     if idx1 == sLen or idx2==tLen:
        #         return 1 if idx2 == tLen else 0
            
        #     if dp[idx1][idx2] != -1:
        #         return dp[idx1][idx2]
            
        #     take = 0
        #     if s[idx1] == t[idx2]:
        #         take = solve(idx1+1,idx2+1)
        #     skip = solve(idx1+1,idx2)
        #     dp[idx1][idx2] =  take+skip
        #     return dp[idx1][idx2]
        # return solve(0,0)
  # tabulation or bottom-up approach
        # T.C:O(N*M)
        # S.C:O(N*M) 
        dp = [[0] * (tLen+1) for _ in range(sLen+1)]
        for i in range(sLen+1):
            dp[i][tLen] = 1

        for idx1 in range(sLen-1,-1,-1):
            for idx2 in range(tLen-1,-1,-1):
                take = 0
                if s[idx1] == t[idx2]:
                    take = dp[idx1+1][idx2+1]
                skip = dp[idx1+1][idx2]
                dp[idx1][idx2] =  take+skip
        return dp[0][0]

        



            
        