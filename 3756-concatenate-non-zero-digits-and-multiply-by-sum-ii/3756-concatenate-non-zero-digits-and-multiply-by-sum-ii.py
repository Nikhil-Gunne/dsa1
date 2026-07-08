class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        n = len(s)

        cnt = [0] * n

        prefNum = [0]
        prefSum = [0]

        c = 0

        for i, ch in enumerate(s):
            if ch != '0':
                d = ord(ch) - ord('0')

                c += 1
                prefNum.append((prefNum[-1] * 10 + d) % MOD)
                prefSum.append(prefSum[-1] + d)

            cnt[i] = c

        # powers of 10 modulo MOD
        pow10 = [1] * (c + 1)
        for i in range(1, c + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        ans = []

        for s, e in queries:

            left = cnt[s - 1] if s > 0 else 0
            right = cnt[e]

            length = right - left

            digit_sum = prefSum[right] - prefSum[left]

            number = (
                prefNum[right]
                - prefNum[left] * pow10[length]
            ) % MOD

            ans.append((digit_sum * number) % MOD)

        return ans