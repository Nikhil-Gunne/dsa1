class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cnt = 0
        for i in costs:
            if coins - i >= 0:
                cnt += 1

                coins -= i
            else:
                break
        return cnt
        