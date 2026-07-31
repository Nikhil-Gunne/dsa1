class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = Counter(s)
        mxHeap = []
        for i in freq:
            heappush(mxHeap,(-freq[i],i))
        
        res = ""
        while mxHeap:
            cnt,char = heappop(mxHeap)
            res += char * (-1*cnt)
        return res

