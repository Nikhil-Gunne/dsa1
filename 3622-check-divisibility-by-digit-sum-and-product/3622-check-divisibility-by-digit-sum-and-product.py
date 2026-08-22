class Solution:
    def checkDivisibility(self, n: int) -> bool:

        dSum = 0
        dProd = 1
        temp = n
        while temp:
            rem = temp % 10
            dSum += rem
            dProd *= rem
            temp //=10
        return n % (dSum +dProd) == 0
        