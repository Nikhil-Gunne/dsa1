class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd1(a,b):
            if a==1 or b==1:
                return 1
            
            if a == 0:
                return b
            
            if a > b:
                a,b = b,a

            return gcd1(b%a,a)
        mxEl = 0
        minEl = 1001

        for i in nums:
            mxEl = max(mxEl,i)
            minEl = min(minEl,i)
        
        return gcd1(minEl,mxEl)
        