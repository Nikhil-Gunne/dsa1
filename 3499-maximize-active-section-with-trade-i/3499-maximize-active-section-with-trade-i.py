class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:

        prevBlock = 0
        currBlock =0
        onesBlock = 0
        res = 0

        totalOnes = s.count('1')
        s+='1'
        for i in s:
            if i == '0':
                currBlock += 1
            else:
                if prevBlock > 0 and currBlock > 0  and onesBlock > 0:
                    # res = max(res,prevBlock+currBlock+onesBlock+(totalOnes-onesBlock))
                    res = max(res,prevBlock+currBlock+totalOnes)

                    onesBlock = 0

                if currBlock > 0:
                    prevBlock = currBlock
                    currBlock = 0
                onesBlock += 1
        return max(res,totalOnes)



        