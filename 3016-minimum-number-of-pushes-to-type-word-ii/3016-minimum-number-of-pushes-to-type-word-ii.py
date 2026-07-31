class Solution:
    def minimumPushes(self, word: str) -> int:

        freq = [0] *26
        for i in word:
            freq[ord(i)-97] +=1
        
        freq.sort(reverse = True)
        places = 1
        cnt = 0
        presses = 0
        for i in range(26):
            if freq[i] == 0:
                break
            presses += (freq[i]*places)
            cnt+=1
            if cnt % 8 == 0:
                places += 1
        return presses


        