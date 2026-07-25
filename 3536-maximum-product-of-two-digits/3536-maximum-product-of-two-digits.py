class Solution:
    def maxProduct(self, n: int) -> int:
        mx1 = 0
        mx2 = 0

        while n:
            rem = n % 10
            if rem > mx1:
                mx2 = mx1
                mx1= rem
            elif rem > mx2:
                mx2 = rem
            n //=10
        return mx1*mx2
                