class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0],-x[1]))
        cnt = 0
        n = len(intervals)
        end = intervals[0][1]
        for i in range(1,n):
            _,end1 = intervals[i]
            if end1 <= end:
                cnt+=1
            end = max(end,end1)
        
        return n-cnt

        