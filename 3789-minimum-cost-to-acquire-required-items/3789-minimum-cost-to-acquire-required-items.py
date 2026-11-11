class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        sep2 = cost1 + cost2
        res = min(need1,need2) * min(sep2,costBoth)
        # print(res)
        rem = abs(need1-need2) * min((cost1 if need1 > need2 else cost2),costBoth)
        # print(rem)
        return res + rem
        