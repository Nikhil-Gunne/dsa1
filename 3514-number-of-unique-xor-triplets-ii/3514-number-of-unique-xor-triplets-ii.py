class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:

        pairs = set()
        n = len(nums)
        if n==1:
            return n
        mxEl = max(nums)
        for i in range(n):
            for j in range(i+1,n):
                pairs.add(nums[i] ^ nums[j])
        
        sz = 1
        while sz <= mxEl:
            sz*=2
        
        poss = [0] * sz
        for i in nums:
            for j in pairs:
                poss[i^j] = 1
        
        return sum(poss)
        
        
        