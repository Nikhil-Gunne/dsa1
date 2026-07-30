class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        pairs = []
        for i in freq:
            heappush(pairs,(-freq[i],i))
        res = []
        for _ in range(k):
            _,ele = heappop(pairs)
            res.append(ele)

        
        return res
        
    