from sortedcontainers import SortedList

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        sl = SortedList()
        sl.add(0)  
        
        cnt = 0
        P = 0
        for k in range(n):
            P += 1 if nums[k] == target else -1
            cnt += sl.bisect_left(P)
            sl.add(P)
        return cnt