class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minIdx = 0
        maxIdx = 0

        n = len(nums)

        for i in range(n):
            if nums[i] < nums[minIdx]:
                minIdx = i

            if nums[i] > nums[maxIdx]:
                maxIdx = i

        left = min(minIdx, maxIdx)
        right = max(minIdx, maxIdx)

        return min( right + 1,n - left,left + 1 + n - right )