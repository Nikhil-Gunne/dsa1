class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        requestsHandled = [0] * k
        busyServers = []
        freeServers = SortedList(range(k))
        
        n = len(arrival)
        for i in range(n):
            while busyServers and busyServers[0][0] <= arrival[i]:
                freeServers.add(heappop(busyServers)[1])

            if i % k in freeServers:
                freeServers.remove(i%k)
                requestsHandled[i%k] += 1
                heappush(busyServers,(arrival[i] + load[i],i%k))
            else:
                idx = freeServers.bisect_right(i % k)
                
                if len(freeServers)==0:
                    continue
                if idx==len(freeServers):
                    idx = 0
                requestsHandled[freeServers[idx]]+=1
                heappush(busyServers,(arrival[i] + load[i],freeServers[idx]))
                freeServers.pop(idx)
        print(requestsHandled)
        res = []
        maxReqs = max(requestsHandled)
        for i in range(k):
            if requestsHandled[i] == maxReqs:
                res.append(i)

                
        return res
        