class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:


        return gcd(n*n,n*(n+1))
        # oddSum = 0
        # evenSum = 0
        # for i in range(1,(n*2)+1):
        #     oddSum += i if i &1 else 0
        #     evenSum += i if i & 1 == 0 else 0
        
        # return gcd(oddSum,evenSum)
        