class Solution:
    def minMoves2(self, nums: list[int]) -> int:

        nums.sort()
        n = len(nums)
        mid = n//2
        ops = 0
        for i in nums:
            ops += abs(i-nums[mid])
        return ops
        