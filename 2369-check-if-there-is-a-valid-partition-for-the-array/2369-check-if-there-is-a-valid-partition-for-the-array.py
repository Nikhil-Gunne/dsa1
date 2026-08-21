class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [-1] * n
        def solve(idx):
            if idx>=n:
                return True
            if dp[idx] != -1:
                return dp[idx]
            res = False
            if idx+1 < n and nums[idx] == nums[idx+1]:
                res = res | solve(idx+2)
                if res:
                    dp[idx] = res
                    return dp[idx]
            if idx+2 < n and nums[idx] == nums[idx+1] and nums[idx+1] == nums[idx+2]:
                res = res | solve(idx+3)
                if res:
                    dp[idx] = res
                    return dp[idx]
            if idx + 2 < n and nums[idx+1] - nums[idx] == 1 and nums[idx+2] - nums[idx+1] == 1:
                res = res | solve(idx+3)
                if res:
                    dp[idx] = res
                    return dp[idx]
            dp[idx] = res
            return dp[idx]
        return solve(0)
            


        