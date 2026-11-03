class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxEl = max(nums)
        ops = 0
        for i in nums:
            ops += maxEl - i
        return ops
        