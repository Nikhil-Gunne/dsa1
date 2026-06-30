class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        totalSum = sum(nums)
        leftSum = 0
        res = []
        for i in nums:
            totalSum -= i
            res.append(abs(totalSum-leftSum))
            leftSum+=i
        return res
        