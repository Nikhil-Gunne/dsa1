class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        self.maxLen = 0
        self.res = set()
        n = len(s)
        
        def solve(idx,curr,open):
            if idx == n:
                currLen = len(curr)
                # print(curr,currLen)
                if  currLen >= self.maxLen and open == 0:
                    if currLen == self.maxLen:
                        self.res.add(curr)
                    else:
                        self.res = set([curr])
                        self.maxLen = currLen
                return
            
            if s[idx] == '(':
                solve(idx+1 , curr, open)
                solve(idx+1 , curr + s[idx] , open + ( 1 if s[idx] == '(' else 0))
            elif s[idx] == ')':
                solve(idx+1 , curr, open)
                if open > 0:
                    solve(idx+1,curr + ')',open-1)
            else:
                solve(idx+1 , curr + s[idx] , open)


        
        solve(0,"",0)
        return list(self.res)
                
