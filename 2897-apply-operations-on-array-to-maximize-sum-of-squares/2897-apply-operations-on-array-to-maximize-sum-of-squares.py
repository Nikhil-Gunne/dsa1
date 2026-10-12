class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        

        bitFreq = [0] *32
        mod = 10**9+7
        for i in nums:
            for j in range(32):
                if i & 1<<j:
                    bitFreq[j] += 1
        
        res = 0
        while k:
            num = 0
            for i in range(32):
                if bitFreq[i]:
                    num = num | 1<<i
                    bitFreq[i]-=1
            k-=1
            res += (num * num) % mod
        return res % mod


