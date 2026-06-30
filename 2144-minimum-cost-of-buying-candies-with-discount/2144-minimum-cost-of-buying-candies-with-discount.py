class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)

        c = 0
        cnt = 0

        for i in range(len(cost)):
            if cnt == 2:
                cnt = 0
                continue

            cnt += 1
            c += cost[i]

            # print(i, c)

        return c
        