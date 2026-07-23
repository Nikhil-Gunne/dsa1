class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n
        def bitCount(num):
            cnt = 0
            while num:
                cnt+=1
                num>>=1
            return cnt
        return 2**bitCount(n)
        