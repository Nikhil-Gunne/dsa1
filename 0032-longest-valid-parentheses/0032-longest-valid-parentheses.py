class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0

        
        open = close = 0

        for ch in s:
            if ch == '(':
                open += 1
            else:
                close += 1

            if open == close:
                ans = max(ans, 2 * close)
            elif close > open:
                open = close = 0

        
        open = close = 0

        for ch in reversed(s):
            if ch == '(':
                open += 1
            else:
                close += 1

            if open == close:
                ans = max(ans, 2 * open)
            elif open > close:
                open = close = 0

        return ans