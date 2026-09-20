class Solution:
    def reverseDegree(self, s: str) -> int:
        
        res = 0
        for i in range(len(s)):
           
            pos = 123 - ord(s[i])
            
            res = res + ( pos * (i+1) )
        return res
        