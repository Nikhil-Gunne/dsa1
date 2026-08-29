class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        pairs = [(nums[i],i) for i in range(n)]
        pairs.sort()
        groupVals = defaultdict(list)
        groupIdxs = defaultdict(SortedList)
        group = 0
        groupVals[group].append(pairs[0][0])
        groupIdxs[group].add(pairs[0][1])
        
        for i in range(n-1):
            if pairs[i+1][0]-pairs[i][0] <= limit:
                groupVals[group].append(pairs[i+1][0])
                groupIdxs[group].add(pairs[i+1][1])
            else:
                group += 1
                groupVals[group].append(pairs[i+1][0])
                groupIdxs[group].add(pairs[i+1][1])
        
        # print(groupIdxs)
        # print(groupVals)
        res = [0] * n
        for i in range(group+1):
            idx = 0
            while idx < len(groupVals[i]):
                res[groupIdxs[i][idx]] = groupVals[i][idx]
                idx+=1
            

        return res
        

            
        