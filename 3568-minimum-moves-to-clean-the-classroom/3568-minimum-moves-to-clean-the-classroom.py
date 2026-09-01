class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        rows = len(classroom)
        cols = len(classroom[0])

        sr = sc = -1
        litters = 0
        littersMap = {}

        for i in range(rows):
            for j in range(cols):
                if classroom[i][j] == 'S':
                    sr = i
                    sc = j

                elif classroom[i][j] == 'L':
                    littersMap[(i, j)] = litters
                    litters += 1

        if litters == 0:
            return 0

        fullMask = (1 << litters) - 1

        q = deque([(sr, sc, energy, 0, 0)])
        visited = {(sr, sc, energy, 0)}

        directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]

        while q:

            r, c, currEn, mask, moves = q.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                if classroom[nr][nc] == 'X':
                    continue


                newEn = currEn - 1


                if newEn < 0:
                    continue

                newMask = mask


                if classroom[nr][nc] == 'L':
                    newMask |= (1 << littersMap[(nr, nc)])


                if classroom[nr][nc] == 'R':
                    newEn = energy


                if newMask == fullMask:
                    return moves + 1

                state = (nr, nc, newEn, newMask)

                if state in visited:
                    continue

                visited.add(state)

                q.append((nr, nc, newEn, newMask, moves + 1))

        return -1