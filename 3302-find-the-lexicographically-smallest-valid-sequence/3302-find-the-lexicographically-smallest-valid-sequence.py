class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m = len(word1)
        n = len(word2)
        rightCnt = [0] * m
        j = n -1
        cnt = 0
        for i in range(m-1,-1,-1):
            if word2[j] == word1[i]:
                cnt += 1
                j-=1 if j>0 else 0
            rightCnt[i] = cnt
            
        
        # if i>0:
        #     temp = i
        #     while temp>0:
        #         rightCnt[temp] = cnt
        #         temp-=1

        
        
        # print(rightCnt)
        used = False
        res = []
        j=0
        for i in range(m):
            # print(i,j)
            if word1[i] == word2[j]:
                res.append(i)
                j+=1
            elif not used and i<m-1 and rightCnt[i+1]>=(n-j-1):
                res.append(i)
                j+=1
                used = True
            if j==n:
                break
        return res if j==n else []
        


        