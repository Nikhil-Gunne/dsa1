class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def getGcd(start,end):
            # print(start,end)
            ans = nums[start]
            for i in range(start+1,end):
                ans = gcd(ans,nums[i])
            return ans
        def getLcm(start,end):
            ans = nums[start]
            for i in range(start+1,end):
                ans = lcm(ans,nums[i])
            return ans

        def getPr(start,end):
            ans = nums[start]
            for i in range(start+1,end):
                ans *= nums[i]
            return ans
        res = 0
        for i in range(1,len(nums)+1):
            for j in range(len(nums)-i+1):
                # print(i,getPr(j,j+i),getGcd(j,j+i) * getLcm(j,j+i))
                if getPr(j,j+i) == getGcd(j,j+i) * getLcm(j,j+i):
                    res = i
        return res
                
            
            
        