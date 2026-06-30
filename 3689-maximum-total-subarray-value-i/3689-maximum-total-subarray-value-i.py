class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxNum = 0
        minNum = float('inf')
        for i in nums:
            maxNum = max(maxNum,i) 
            minNum = min(minNum,i)
        return (maxNum - minNum ) *k
        