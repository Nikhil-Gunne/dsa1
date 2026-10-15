class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        


        res = 0
        n = len(nums)
        for i in range(n):
            temp = set()
            for j in range(i,n):
                temp.add(nums[j])
                res += len(temp) ** 2
        return res
