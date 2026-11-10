class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        

        dp = [-1] * n

        def solve(idx):
            # print(idx)
            if idx == n:
                return 0
            
            if dp[idx] != -1:
                return dp[idx]
            
            res = float('inf')
            for i in range(idx+1,min(idx+4,n+1)):
                res = min(res,costs[i-1]+((idx-i)**2) + solve(i))
            dp[idx] = res
            return dp[idx]
        
        solve(0)
        return dp[0]

        