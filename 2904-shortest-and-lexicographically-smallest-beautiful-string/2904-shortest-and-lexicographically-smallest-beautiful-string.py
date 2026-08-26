class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        

        sIdx = 0
        eIdx = -1

        left = 0
        onesCount  =0
        for right in range(len(s)):
            if s[right] == '1':
                onesCount += 1
            
            while onesCount >= k:
                if eIdx == -1 or (right - left < eIdx-sIdx) :
                    sIdx = left
                    eIdx = right
                elif (right-left == eIdx-sIdx) and s[left:right+1] < s[sIdx:eIdx+1]:
                    sIdx = left
                    eIdx = right
                
                if s[left] == '1':
                    onesCount-=1
                left+=1
        
        return s[sIdx:eIdx+1] if eIdx != -1 else ""


        