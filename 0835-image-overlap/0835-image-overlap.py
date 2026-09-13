class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        n = len(img1)


        def overLapCount(r,c):
            cnt = 0
            for i in range(n):
                for j in range(n):
                    dr = i + r
                    dc = j + c
                    if min(dr,dc) < 0 or dr >= n or dc >= n:
                        continue
                    # print(dr,dc)
                    if img1[i][j] & img2[dr][dc]:
                        cnt += 1
            return cnt

        res = 0
        for rowOffset in range(-n+1,n):
            for colOffset in range(-n+1,n):
                res = max(res,overLapCount(rowOffset,colOffset))
        return res

        