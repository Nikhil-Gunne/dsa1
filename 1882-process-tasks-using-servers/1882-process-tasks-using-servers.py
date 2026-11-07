class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        freeServers = []
        for idx,server in enumerate(servers):
            heappush(freeServers,(server,idx))
        n = len(tasks)
        res = [0] * n
        usedServers = []
        time = 0
        for i in range(n):
            time = max(time,i)
            while usedServers and usedServers[0][0] <= i:
                _,serverWt,serverIdx = heappop(usedServers)
                heappush(freeServers,(serverWt,serverIdx ))
            
                
            
            if len(freeServers) == 0:
                time = usedServers[0][0]
                while usedServers and usedServers[0][0] <= time:
                    _,serverWt,serverIdx = heappop(usedServers)
                    heappush(freeServers,(serverWt,serverIdx ))
                
            freeServer,freeIdx = heappop(freeServers)
            heappush(usedServers,(time+tasks[i],freeServer,freeIdx))
            res[i] = freeIdx
        return res







        