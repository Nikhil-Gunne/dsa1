class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        dp = {}

        def solve(stones, turn):
            if stones == 0:
                return True if turn == 0 else False

            if (stones, turn) in dp:
                return dp[(stones, turn)]

            if turn == 1:  # Alice
                res = False

                for i in range(1, int(stones ** 0.5) + 1):
                    res = res or solve(stones - i * i, turn ^ 1)

                    if res:
                        break

            else:  # Bob
                res = True

                for i in range(1, int(stones ** 0.5) + 1):
                    res = res and solve(stones - i * i, turn ^ 1)

                    if not res:
                        break

            dp[(stones, turn)] = res
            return res

        return solve(n, 1)