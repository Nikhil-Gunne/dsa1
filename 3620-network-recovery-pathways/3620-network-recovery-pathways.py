
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = defaultdict(list)
        low = float('inf')
        high = float('-inf')
        for u, v, cost in edges:
            if not online[u] or not online[v]:
                continue
            low = min(low,cost)
            high = max(high,cost)
            graph[u].append((v,cost))
        
        def isPossible(val):
            q = [(0,0)]
            dist = [float('inf')] * n
            while q:
                cost,curr = heappop(q)
                if curr == n-1:
                    return True
                if dist[curr]<cost:
                    continue
                for v,cost1 in graph[curr]:
                    if cost1 < val:
                        continue
                    
                    if cost+cost1 <= k and cost+cost1<dist[v]:
                        dist[v] = cost+cost1
                        heappush(q,(cost+cost1,v))
            return False
        
        ans = -1
        while low <= high:
            mid = low + ((high-low)//2)

            if isPossible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
            

        