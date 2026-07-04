class DSU:
    def __init__(self,n):
        self.parent = [ i for i in range(n+1) ]
        self.size = [ 1 for _ in range(n+1) ]
        self.dist = [float('inf')] * (n+1)
    
    def findParent(self,node):
        if self.parent[node] != node:
            self.parent[node]= self.findParent(self.parent[node])
            return self.parent[node]
        return node
    
    def unionBySize(self,u,v,dist):
        par_u = self.findParent(u)
        par_v = self.findParent(v)

        if par_u == par_v:
            self.dist[par_u] = min(self.dist[par_v],dist,self.dist[par_u])
            return
        
        if self.size[par_u]<self.size[par_v]:
            self.parent[par_u] = par_v
            self.size[par_v] += self.size[par_u]
            self.dist[par_v] = min(self.dist[par_v],dist,self.dist[par_u])
        else:
            self.parent[par_v] = par_u
            self.size[par_u] += self.size[par_v]
            self.dist[par_u] = min(self.dist[par_v],dist,self.dist[par_u])
        

        
    
   
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # dsu = DSU(n)

        # for u,v,d in roads:
        #     dsu.unionBySize(u,v,d)
        
        # par_1 = dsu.findParent(1)
        # # par_2 = dsu.findParent(n)

        # return dsu.dist[par_1] 

       

        graph = defaultdict(list)

        for u,v,d in roads:
            graph[u].append((v,d))
            graph[v].append((u,d))
        
        q = deque([1])
        visited = set()
        visited.add(1)
        res = float('inf')
        while q:
            curr = q.popleft()
            for v,d in graph[curr]:
                res = min(res,d)
                if v not in visited:
                    visited.add(v)
                    q.append((v))
        return res
        

        