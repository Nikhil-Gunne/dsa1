class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        minSm = float('inf')
        for i in range(n):
            sm = 0
            for j in range(i,n):
                sm += nums[j]
                # print(sm)
                if l<=j-i+1<=r and sm>0:
                    minSm = min(sm,minSm)
                    # print(minSm)
        return minSm if minSm != float('inf') else -1


        