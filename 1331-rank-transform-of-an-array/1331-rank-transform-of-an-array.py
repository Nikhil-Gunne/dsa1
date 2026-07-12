class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(set(arr))
        idxMap = {temp[i]: i for i in range(len(temp))}

        res = []
        for i in arr:
            res.append(idxMap[i]+1)
        return res

        