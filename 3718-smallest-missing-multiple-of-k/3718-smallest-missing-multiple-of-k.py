class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        nums = set(nums)
        mult = 1
        while k * mult in nums:
            mult +=1
        return k*mult
        