class Solution:
    def processStr(self, s: str, k: int) -> str:
        
        l = 0
        n = len(s)
        for i in range(n):
            if s[i] == '*':
                if l>0:
                    l-=1
            elif s[i] == '#':
                l *= 2
            elif s[i] == '%':
                pass
            else:
                l+=1
        if k>=l:
            return '.'
        for i in range(n-1,-1,-1):
            if s[i] == '*':
                l+=1
            elif s[i] == '#':
                l //= 2
                if k >= l:
                    k = k-l
            elif s[i]=='%':
                k = l-k-1
            else:
                l-=1
            if l==k:
                return s[i]
        return '.'

