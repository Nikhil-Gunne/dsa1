class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return n
        sm = 0
        temp = ""
       
        while n:
            rem = n % 10
            if rem>0:
                temp += str(rem)
            sm += rem
            
            n//=10
            
        return sm * int(temp[::-1])

        