class Solution:
    def gcdSum(self, nums: list[int]) -> int:

        def gcd1(a,b):
            if a==1 or b==1:
                return 1
            
            if a == 0:
                return b
            
            if a > b:
                a,b = b,a
            return gcd1(b%a,a)

        gcds = []
        mxEl = 0
        for i in nums:
            mxEl =max(mxEl,i)
            gcds.append(gcd1(mxEl,i))
        
        gcds.sort()
        # print(gcds)
        sm = 0
        left = 0
        right = len(gcds)-1
        while left<right:
            sm += gcd1(gcds[left],gcds[right])
            left += 1
            right -=1
        return sm



        