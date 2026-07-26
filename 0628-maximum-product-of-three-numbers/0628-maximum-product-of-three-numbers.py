class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        mx1 = mx2 = mx3 = float('-inf')
        mn1 = mn2 = float('inf')

        for i in nums:
            if i > mx1:
                mx3 = mx2
                mx2 = mx1
                mx1 = i
            elif i > mx2:
                mx3 = mx2
                mx2 = i
            elif i>mx3:
                mx3 = i
            
            if i < mn1:
                mn2 = mn1
                mn1 = i
            elif i < mn2:
                mn2 = i
        return max(mx1*mx2*mx3,mn1*mn2*mx1)
        # nums.sort()
        # res = float('-inf')
        # if nums[1] < 0:
        #     res = max(res,nums[0]*nums[1]*nums[-1])

        # return max(res,nums[-3]*nums[-2]*nums[-1])