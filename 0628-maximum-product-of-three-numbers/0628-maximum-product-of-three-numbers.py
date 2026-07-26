class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        res = float('-inf')
        if nums[1] < 0:
            res = max(res,nums[0]*nums[1]*nums[-1])

        return max(res,nums[-3]*nums[-2]*nums[-1])