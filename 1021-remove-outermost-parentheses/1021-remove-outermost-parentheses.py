class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0

        left = 0
        res = ''
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -=1
            
            if depth == 0:
                if left+1 < i:
                    res += s[left+1:i]
                left = i+1
        return res

        