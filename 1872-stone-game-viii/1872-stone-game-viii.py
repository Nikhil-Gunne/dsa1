class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:


        n = len(stones)
        pref = [0] *n
        pref[0] = stones[0]
        
        for i in range(1,n):
            pref[i] = pref[i-1] + stones[i] 
            

        dp = [float('-inf')] * n
        def solve(idx):
            if idx == n-1:
                return pref[idx]
            
            if dp[idx] != float('-inf'):
                return dp[idx]
            
            take = pref[idx] - solve(idx+1)
            skip = solve(idx+1)
            dp[idx] = max(take,skip)
            return dp[idx]
        return solve(1)
        


        