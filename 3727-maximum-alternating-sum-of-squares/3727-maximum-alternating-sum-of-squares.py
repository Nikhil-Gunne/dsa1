class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:


        
        nums.sort( key = lambda x : abs(x))
        n = len(nums)
        res = 0
        left = 0
        right = n-1
        if n %2 :
            res += nums[right] * nums[right]
            right-=1
        
        while left<right:
            res += (nums[right]*nums[right]) - (nums[left]*nums[left])
            left+=1
            right -=1
        return res
        

        


        