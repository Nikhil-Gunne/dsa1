class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((v,t))
        
        visited = set()
        minHeap = [(0,k)]
        res = 0
        while minHeap:
            currTime,node = heappop(minHeap)
            if node in visited:
                continue
            res = max(res,currTime)
            visited.add(node)
            for nei,time in graph[node]:
                if nei not in visited:
                    heappush(minHeap,(currTime+time,nei))
        return res if len(visited) == n else -1

