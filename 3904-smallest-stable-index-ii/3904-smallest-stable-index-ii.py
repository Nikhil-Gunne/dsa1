class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffixMin = [0] * n
        suffixMin[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            suffixMin[i] = min(suffixMin[i+1],nums[i])
        
        currMax = 0
        for i in range(n):
            currMax = max(currMax,nums[i])
            if currMax-suffixMin[i] <= k:
                return i
        return -1