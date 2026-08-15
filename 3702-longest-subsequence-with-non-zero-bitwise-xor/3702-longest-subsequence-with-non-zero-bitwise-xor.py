class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)

        totalXor = 0
        hasNonZero = False

        for num in nums:
            totalXor ^= num

            if num != 0:
                hasNonZero = True

        if totalXor != 0:
            return n

        if hasNonZero:
            return n - 1

        return 0