class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if n==1:
            return 0
        is_sorted = True
        mid_max = s[1]
        mid_min = s[1]

        minEl = s[0]
        maxEl = s[0]

        for i in range(1,n):
            if s[i] < s[i-1]:
                is_sorted = False
            if i != n-1:
                mid_max = max(mid_max,s[i])
                mid_min = min(mid_min,s[i])
            minEl = min(minEl,s[i])
            maxEl = max(maxEl,s[i])
        
        if is_sorted:
            return 0
            
        if n == 2:
            return -1
        
        if s[0] == minEl or s[n-1] == maxEl:
            return 1
        
        
        if s[0] > mid_max and s[n-1] < mid_min:
            return 3
        return 2
        