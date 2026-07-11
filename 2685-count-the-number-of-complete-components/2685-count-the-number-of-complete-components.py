class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        graph =  defaultdict(list)
        indeg = [0] * n
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indeg[u] += 1
            indeg[v] += 1
        
        visited = [False] * n

        def bfs(node):
            visited[node] = True
            q = deque()
            q.append(node)
            maxEdges = 0
            minEdges = n
            cnt = 0
            while q:
                curr = q.popleft()
                cnt += 1
                maxEdges = max(maxEdges,indeg[curr])
                minEdges = min(minEdges,indeg[curr])
                for nei in graph[curr]:
                    if not visited[nei]:
                        q.append(nei)
                        visited[nei] = True
            return maxEdges == cnt-1 and minEdges == cnt-1
        
        res = 0
        for i in range(n):
            if not visited[i] and bfs(i):
                res+=1
        return res



        