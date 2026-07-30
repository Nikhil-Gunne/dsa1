class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        row = rows-1
        col = 0

        while row >= 0 and col < cols:
            dR = row
            dC = col

            temp = []
            while dR < rows and dC < cols:
                temp.append(mat[dR][dC])
                dR += 1
                dC += 1
            temp.sort()

            dR = row
            dC = col
            idx = 0
            while dR < rows and dC < cols:
                mat[dR][dC] = temp[idx]
                idx+=1
                dR += 1
                dC += 1

            if row > 0:
                row -= 1
            else:
                col += 1
        return mat

        