class Solution:
    def canAliceWin(self, n: int) -> bool:
        curr = 10
        turn  = 'A'
        while curr <= n:
            turn = ('B' if turn == 'A' else 'A')
            n-=curr
            curr -= 1
        return turn == 'B'
        