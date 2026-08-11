class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        sm = nums[0]
        for i in range(1,n):
            if nums[i]-1 == nums[i-1]:
                sm += nums[i]
            else:
                break
        seen= set(nums)
        while sm in seen:
            sm+=1
            

        return sm