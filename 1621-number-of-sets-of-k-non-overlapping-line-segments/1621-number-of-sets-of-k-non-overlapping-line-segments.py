class Solution:
    def numberOfSets(self, n: int, k: int) -> int:

        dp = [[0] * (n + 1) for _ in range(k + 1)]
        mod = 10**9 + 7

        for i in range(n + 1):
            dp[0][i] = 1


        for k1 in range(1, k + 1):
            prevRow = [0] * (n + 1)

            
            for i in range(n - 1, -1, -1):
                prevRow[i] = (prevRow[i + 1] + dp[k1-1][i]) % mod

            for i in range(n - 1, -1, -1):
                skip = dp[k1][i + 1]
                take = prevRow[i + 1]

                dp[k1][i] = (take + skip) % mod

            

        return dp[k][0]

        # def solve(k1,i):
        #     if k1 == 0:
        #         return 1
        #     if i >= n:
        #         return 0
            
        #     skip = solve(k1,i+1)
        #     take = 0
        #     for j in range(i+1,n):
        #         take = take + solve(k1-1,j)
        #     return take + skip
        # return solve(k,0)

        