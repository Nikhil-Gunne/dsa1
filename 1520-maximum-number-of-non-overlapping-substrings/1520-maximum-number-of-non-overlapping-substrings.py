class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        start = [-1] * 26
        end = [0] * 26
        isValid = [True] * n

        for i in range(n):
            pos = ord(s[i])-97
            if start[pos] == -1:
                start[pos] = i
            end[pos] = max(end[pos],i)
        
        for c in range(26):
            if start[c] ==-1:
                continue
            idx = start[c]
            while idx  < end[c]+1:
                pos = ord(s[idx])-97
                if start[pos] < start[c]:
                    isValid[start[c]] = False
                    break
                end[c] = max(end[c],end[pos])
                idx+=1
        
        res = []
        prevUsedIdx = n
        for idx in range(n-1,-1,-1):
            pos = ord(s[idx]) - 97
            if isValid[idx] and start[pos] == idx and end[pos] < prevUsedIdx:
                res.append(s[start[pos]:end[pos]+1])
                prevUsedIdx = idx
        return res


