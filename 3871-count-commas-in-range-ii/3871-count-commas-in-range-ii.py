

class Solution:
    def countCommas(self, n: int) -> int:
        # digitCnt = int(log10(n)) + 1
        digitCnt = len(str(n))

        if digitCnt < 4:
            return 0

        cnt = 0

        for i in range(4, digitCnt + 1):
            commas = (i - 1) // 3

            lower = 10 ** (i - 1)
            upper = min(n, 10 ** i - 1)

            cnt += commas * (upper - lower + 1)

        return cnt


        