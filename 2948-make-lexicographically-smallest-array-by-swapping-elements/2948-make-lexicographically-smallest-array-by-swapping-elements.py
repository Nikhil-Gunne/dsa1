class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        pairs = [(nums[i],i) for i in range(n)]
        pairs.sort()
        groupVals = defaultdict()
        
        group = 0
        
        groupVals[group]= deque([pairs[0][0]])
        
        idxToGrp = defaultdict(int)
        idxToGrp[pairs[0][1]] = group
        for i in range(n-1):
            if pairs[i+1][0]-pairs[i][0] <= limit:
                groupVals[group].append(pairs[i+1][0])
                idxToGrp[pairs[i+1][1]] = group
            else:
                group += 1
                idxToGrp[pairs[i+1][1]] = group
                groupVals[group] = deque([pairs[i+1][0]])
                
        
        res = []
        
        for i in range(n):
            idxGrp = idxToGrp[i]
            res.append(groupVals[idxGrp].popleft())

        return res
        

            
        