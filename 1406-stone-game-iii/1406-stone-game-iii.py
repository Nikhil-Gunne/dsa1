class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = {}

        def solve(idx):
            if idx >= n:
                return 0

            if idx in dp:
                return dp[idx]

            res = float('-inf')
            currSum = 0

            for i in range(idx, min(n, idx + 3)):
                currSum += stoneValue[i]
                res = max(res, currSum - solve(i + 1))

            dp[idx] = res
            return res

        res = solve(0)

        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        else:
            return "Tie"