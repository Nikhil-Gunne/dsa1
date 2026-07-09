class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def findParent(self,node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    def unionBySize(self,u,v):
        par_u = self.findParent(u)
        par_v = self.findParent(v)
        if self.size[par_u] >= self.size[par_v]:
            self.parent[par_v] = par_u
            self.size[par_u] += self.size[par_v]
        else:
            self.parent[par_u] = par_v
            self.size[par_v] += self.size[par_u]
        


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        for i in range(1,n):
            if nums[i] - nums[i-1] <= maxDiff:
                dsu.unionBySize(i-1,i)
        res = []
        for u,v in queries:
            par_u = dsu.findParent(u)
            par_v = dsu.findParent(v)

            res.append(par_u == par_v)
        return res
               


        # def isPath(curr,src,dest):
        #     if curr <= dest:
        #         return True

        #     left = bisect_left(nums,nums[curr]-maxDiff)
        #     if left == curr:
        #         return False
        #     return isPath(left,left,dest)
        

        # res = []
        # for u,v in queries:
        #     if u > v:
        #         u,v = v,u
            
        #     res.append(isPath(v,v,u))
        # return res

        