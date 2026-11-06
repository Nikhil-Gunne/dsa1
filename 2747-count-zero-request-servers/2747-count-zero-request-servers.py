class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        logs.sort(key = lambda x : x[1])
        qIdxs = [(queries[i],i) for i in range(len(queries))]
        qIdxs.sort()
        left = 0
        right = 0
        print(logs)
        activeServers = {}
        res = [0] * len(queries)
        for q,idx in qIdxs:
            
            while right<len(logs) and   logs[right][1] <= q:
                if logs[right][0] not in activeServers:
                    activeServers[logs[right][0]] = 0
                activeServers[logs[right][0]] += 1
                right += 1
            while left < right and logs[left][1] < q - x:
                activeServers[logs[left][0]]-=1
                if activeServers[logs[left][0]]==0:
                    del activeServers[logs[left][0]]
                left += 1  
            res[idx] = n - len(activeServers)
            # print(activeServers)
            
        return res
            

        