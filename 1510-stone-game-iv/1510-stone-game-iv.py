class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = {}

        def solve(stones):
            if stones == 0:
                return False

            if stones in dp:
                return dp[stones]

            for i in range(1, int(stones ** 0.5) + 1):
                #if we receive false from next state the current player can win as the next player couldn't pick stones
                if not solve(stones - i * i):
                    dp[stones] = True
                    return True

            dp[stones] = False
            return False

        return solve(n)

        # dp = {}

        # def solve(stones, turn):
        #     if stones == 0:
        #         return True if turn == 0 else False

        #     if (stones, turn) in dp:
        #         return dp[(stones, turn)]

        #     if turn == 1:  # Alice
        #         res = False

        #         for i in range(1, int(stones ** 0.5) + 1):
        #             res = res or solve(stones - i * i, turn ^ 1)

        #             if res:
        #                 break

        #     else:  # Bob
        #         res = True

        #         for i in range(1, int(stones ** 0.5) + 1):
        #             res = res and solve(stones - i * i, turn ^ 1)

        #             if not res:
        #                 break

        #     dp[(stones, turn)] = res
        #     return res

        # return solve(n, 1)