class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:

        nums.sort()
        dp = defaultdict(int)
        mx = 1
        for x in nums:
            dp[x + 1] = max(dp[x + 1], dp[x] + 1)
            dp[x] = max(dp[x], dp[x - 1] + 1)
            mx = max(mx,dp[x],dp[x+1])

        return mx