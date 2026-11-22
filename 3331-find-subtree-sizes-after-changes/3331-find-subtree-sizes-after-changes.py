
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        sizes = [1] * n

        adjList = defaultdict(list)

        for i in range(1,n):
            adjList[parent[i]].append(i)
        

        seen = {}

        def dfs(node):

            ancestor = seen.get(s[node],-1)
            seen[s[node]] = node
            
            for child in adjList[node]:
                dfs(child)
                
                
            seen[s[node]] = ancestor
            newPar = parent[node]
            if node != 0:
                if ancestor != -1:
                    newPar = ancestor
                parent[node] = newPar
                sizes[newPar] += sizes[node]

        
        dfs(0)
        return sizes

