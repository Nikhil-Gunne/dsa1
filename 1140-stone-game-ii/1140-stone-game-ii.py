class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = {}
        def solve(idx, x, turn):
            if idx == n:
                return 0
            
            if (idx,x,turn) in dp:
                return dp[(idx,x,turn)]

            if turn:
                res = float('-inf')
            else:
                res = float('inf')

            curr = 0

            for i in range(idx, min(idx + 2 * x, n)):
                curr += piles[i]

                if turn:
                    res = max(
                        res,
                        curr + solve(i + 1, max(i - idx + 1, x), turn ^ 1)
                    )
                else:
                    res = min(
                        res,
                        solve(i + 1, max(i - idx + 1, x), turn ^ 1)
                    )
            dp[(idx,x,turn)] = res
            return res

        return solve(0, 1, 1)