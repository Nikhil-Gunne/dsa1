class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        

        res = []
        depth = 0
        for i in seq:
            if i == '(':
                depth +=1
                res.append(depth % 2)
            else:
                res.append(depth%2)
                depth-=1
        return res        