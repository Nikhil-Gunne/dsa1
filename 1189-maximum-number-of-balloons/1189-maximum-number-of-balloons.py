class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = defaultdict(int)

        for i in text:
            freq[i] +=1 
        poss = -1
        for ch in 'balon':
            if freq[ch] == 0:
                return 0
            
            if ch == 'l' or ch=='o':
                poss = min(poss,freq[ch]//2)
                continue
            if poss == -1:
                poss = freq[ch]
            else:
                poss = min(poss,freq[ch])
        return poss
        