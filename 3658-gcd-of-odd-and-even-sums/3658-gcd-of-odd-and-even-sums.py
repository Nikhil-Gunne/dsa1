class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        def gcd1(a,b):
            # print(a,b)
            if a==1 or b==1:
                return 1
            if a == 0:
                return b
            
            if a > b:
                a,b = b,a
            
            return gcd1(b%a,a)

        
        return gcd1(n*n,n*(n+1))
        # oddSum = 0
        # evenSum = 0
        # for i in range(1,(n*2)+1):
        #     oddSum += i if i &1 else 0
        #     evenSum += i if i & 1 == 0 else 0
        
        # return gcd(oddSum,evenSum)
        