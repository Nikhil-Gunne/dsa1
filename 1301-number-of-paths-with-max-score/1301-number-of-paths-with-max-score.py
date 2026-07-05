class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        

        rows = len(board)
        cols = len(board[0])
        dp = [[[float('-inf'),0] for _ in range(cols+1)] for _ in range(rows+1)]

        dp[rows-1][cols-1] = [0,1]
        mod = (10**9+7)

        for row in range(rows-1,-1,-1):
            for col in range(cols-1,-1,-1):
                if board[row][col] in '123456789':
                    mx = float('-inf')
                    cnt = 0
                    for x,y in [(1,1),(1,0),(0,1)]:
                        dx = row + x
                        dy = col + y
                        if mx < dp[dx][dy][0]:
                            mx = dp[dx][dy][0]
                            cnt = dp[dx][dy][1]
                        elif mx == dp[dx][dy][0]:
                            cnt += dp[dx][dy][1]
                    
                    if mx != float('-inf'):
                        dp[row][col] = [int(board[row][col]) + mx,cnt%mod]
        
        mx = 0
        cnt = 0
        for x,y in [(1,1),(1,0),(0,1)]:
            if mx < dp[x][y][0]:
                mx,cnt = dp[x][y]
            elif mx == dp[x][y][0]:
                cnt += dp[x][y][1]
        return [mx,cnt %(10**9+7)]
        # "brute force wont work for every cell we have 3 paths it will 3^(m*n)"
        # dp = defaultdict(int)
        # self.mx = 0
        # def solve(r,c,sum):
        #     if r == 0 and c == 0:
        #         if sum >= self.mx:
        #             dp[sum] += 1
        #             self.mx = sum
        #         return
        #     if r<0 or c < 0 or board[r][c] == 'X':
        #         return 

        #     solve(r,c-1,sum+int(board[r][c]) if board[r][c] in '123456789' else sum)
        #     solve(r-1,c,sum+int(board[r][c]) if board[r][c] in '123456789' else sum)
        #     solve(r-1,c-1,sum+int(board[r][c]) if board[r][c] in '123456789' else sum)
        
        # solve(len(board)-1,len(board[0])-1,0)
        # return [self.mx,dp[self.mx]]






        

