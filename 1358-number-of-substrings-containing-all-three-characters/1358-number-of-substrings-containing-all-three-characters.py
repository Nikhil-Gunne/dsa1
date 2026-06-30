class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        cnt = 0
        freq = defaultdict(int)
        left = 0
        n = len(s)
        for right in range(n):
            
            freq[s[right]]+=1
            
            while freq and len(freq)==3:
                cnt += (n-right)
                freq[s[left]]-=1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left+=1
        return cnt
        