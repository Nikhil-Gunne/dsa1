class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        res = []
        def solve(curr,o,c):
            if c == n:
                res.append(curr)
                return
            

            if o < n:
                solve(curr + '(',o+1,c)               
            if c < o:
                solve(curr + ')',o,c+1)
        
        solve("",0,0)
        return res