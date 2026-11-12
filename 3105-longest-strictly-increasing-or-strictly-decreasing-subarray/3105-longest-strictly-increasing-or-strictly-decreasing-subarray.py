class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        n = len(nums)
        left = 0
        for i in range(1,n):
            if nums[i] >= nums[i-1]:
                left = i
            ans = max(ans,i-left+1)
        left = 0
        for i in range(1,n):
            if nums[i] <= nums[i-1]:
                left = i
            ans = max(ans,i-left+1)
        return ans

        