class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        cnt = 0
        for i in range(1000,n+1):
            digitCnt = int(log10(i)) 
            # print(i,digitCnt)
            cnt += (digitCnt//3)
        return cnt



        