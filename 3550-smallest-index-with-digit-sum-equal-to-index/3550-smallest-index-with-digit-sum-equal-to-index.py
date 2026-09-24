class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        n = len(nums)
        for i in range(n):
            sm = 0
            temp = nums[i]
            while temp:
                sm += (temp % 10)
                temp//=10
            if sm == i:
                return i
        return -1
        