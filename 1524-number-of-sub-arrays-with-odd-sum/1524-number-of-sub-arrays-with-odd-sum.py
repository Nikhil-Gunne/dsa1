class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        cntOdd = 0
        cntEven = 0
        cSum = 0
        res = 0
        for i in arr:
            cSum += i
            if cSum % 2 == 1:
                res += 1
                res += cntEven
                cntOdd += 1
            else:
                res += cntOdd
                cntEven += 1
        return res % (10**9+7)
            


        