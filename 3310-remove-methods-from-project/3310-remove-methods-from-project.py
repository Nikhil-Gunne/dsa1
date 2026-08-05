class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)

        for a,b in invocations:
            graph[a].append(b)
        
        # bugs = [0] * n

        q = deque([k])
        suspiciousMethods = set()

        while q:
            curr = q.popleft()
            if curr in suspiciousMethods:
                continue
            suspiciousMethods.add(curr)
            # bugs[curr] = 1
            for nei in graph[curr]:
                if nei not in suspiciousMethods:
                    q.append(nei)
        if len(suspiciousMethods) == n:
            return []
        
        
        for u, v in invocations:
            if u not in suspiciousMethods and v in suspiciousMethods:
                return list(range(n))

        
        return [i for i in range(n) if i not in suspiciousMethods]

        # def bfs(node):
        #     q = deque([node])
            
        #     f = 0
        #     while q:
        #         curr = q.popleft()

        #         if curr in suspiciousMethods:
        #             return True
                
        #         if curr in v1:
        #             continue
        #         v1.add(curr)
        #         for nei in graph[curr]:
        #             if nei not in v1:
        #                 q.append(nei)
        #     return False
        # v1 = set()
        # f= 0
        # for i in range(n):
        #     if i not in suspiciousMethods and i not in v1:
        #         temp = bfs(i)
        #         if temp:
        #             f = 1
        #             break
        # res = []
        # if f:
        #     return list(range(n))
        # for i in range(n):
        #     if i not in suspiciousMethods:
        #         res.append(i)
        # return res            

            

        