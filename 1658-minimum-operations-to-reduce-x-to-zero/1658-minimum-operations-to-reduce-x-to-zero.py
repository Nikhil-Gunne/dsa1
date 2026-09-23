class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        n = len(nums)
        target = total - x

        if target < 0:
            return -1
        
        if target == 0:
            return n
        
        left = 0
        cSum = 0
        length = float('inf')
        for right in range(n):
            cSum += nums[right]

            while cSum > target:
                cSum -= nums[left]
                left += 1
            
            if cSum == target:
                length = min(length,n - (right-left+1))
        return length if length != float('inf') else -1