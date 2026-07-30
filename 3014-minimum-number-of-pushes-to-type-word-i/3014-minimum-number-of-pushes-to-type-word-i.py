class Solution:
    def minimumPushes(self, word: str) -> int:
        '''
        xycdefghij
        2 3 4 5 6 7 8 9
        x y c d e f g h
        xi yj
        '''

        presses = 0
        cnt = 0

        for i in word:
            cnt += 1
            presses +=(ceil(cnt/8))
        return presses

        # freq = [0]*26
        # lettersMapped = [0] * 10
        # for i in word:
        #     freq[ord(i)-97] += 1
    
        
        # freq.sort(reverse = True)
        # print(freq)
        # presses = 0
        # for i in range(26):
        #     if freq[i]:
        #         minIdx = 2
        #         curr  = float('inf')
        #         for ii in range(2,10):
        #             if lettersMapped[ii] < curr:
        #                 curr = lettersMapped[ii]
        #                 minIdx = ii 
        #         lettersMapped[minIdx] +=1
        #         # print(i,minIdx)
        #         presses += (freq[i]*lettersMapped[minIdx])
        # return presses
                



        