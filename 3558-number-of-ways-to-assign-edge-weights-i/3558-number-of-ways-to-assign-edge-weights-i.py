class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        hasParent = set()
        mxNode = 0
        for u,v in edges:
            graph[u].append(v)
            hasParent.add(v)
            mxNode = max(mxNode,u,v)
        
        root = -1
        for i in range(1,mxNode+1):
            if i not in hasParent:
                root = i
                break

        q = deque([(root,0)])
        mxDepth = 0
        while q:
            curr,dep = q.popleft()
            mxDepth = max(mxDepth,dep)
            for v in graph[curr]:
                q.append((v,dep+1))
        
        return pow(2,mxDepth-1) %(10**9+7)
            
   

            
        