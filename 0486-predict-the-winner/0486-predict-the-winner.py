class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        dp = {}

        def solve(start,end):
            if start > end:
                return 0
            
            if start == end:
                return nums[start]
            
            if (start,end) in dp:
                return dp[(start,end)]
            
            takeStart = nums[start] - solve(start+1,end)
            takeEnd = nums[end] - solve(start,end-1)
            dp[(start,end)] = max(takeStart,takeEnd)
            return dp[(start,end)]
        
        return solve(0,len(nums)-1) >= 0
        