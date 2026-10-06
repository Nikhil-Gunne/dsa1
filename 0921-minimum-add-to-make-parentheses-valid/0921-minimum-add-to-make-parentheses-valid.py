class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        cnt = 0
        ops = 0
        for i in s:
            if i == '(':
                cnt += 1
            else:
                if cnt > 0:
                    cnt -= 1
                else:
                    ops += 1
        return ops + cnt
        