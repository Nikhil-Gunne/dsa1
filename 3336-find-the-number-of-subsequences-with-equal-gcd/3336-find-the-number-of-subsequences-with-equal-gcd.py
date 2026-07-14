class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10**9+7
        dp = {}
        def solve(idx,first,second):
            if idx == n:
                return first != 0 and first == second

            if (idx,first,second) in dp:
                return dp[(idx,first,second)]
            
            skip = solve(idx+1,first,second)
            seq1Take = solve(idx+1,gcd(first,nums[idx]),second)
            seq2Take = solve(idx+1,first,gcd(second,nums[idx]))

            dp[(idx,first,second)] = (skip + seq1Take + seq2Take ) % mod
            return dp[(idx,first,second)]
        return solve(0,0,0)

        