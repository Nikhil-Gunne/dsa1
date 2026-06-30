class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        target = 1
        for i in arr:
            if i >= target:
                target+=1
        return target-1
        # minHeap = []
        # for i in arr:
        #     heappush(minHeap,i)
        
        # res = 0
        # prev = 0
        # while minHeap:
        #     curr = heappop(minHeap)
        #     if prev == curr: 
        #         res = max(res,curr)
        #         prev = curr
        #     else:
        #         res = max(res,prev+1)
        #         prev = prev + 1
        # return res
