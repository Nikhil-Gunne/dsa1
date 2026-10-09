class Solution:
    def minInsertions(self, s: str) -> int:
        openCount = 0
        idx = 0
        insertions = 0
        n = len(s)
        while idx < n:
            if s[idx] == '(':
                openCount += 1
                idx += 1
            else:
                closingCount = 0
                while idx < n and s[idx] == ')':
                    closingCount += 1
                    idx += 1
                
                
                while closingCount >=2:
                    if openCount:
                        openCount-=1
                    else:
                        insertions += 1
                    closingCount-=2
                    
                
                if closingCount ==1:
                    if openCount:
                        openCount -= 1
                        insertions += 1
                    else:
                        insertions += 2
                        closingCount = 0
                



        return insertions + (openCount * 2)



        