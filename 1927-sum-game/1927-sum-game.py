class Solution:
    def sumGame(self, num: str) -> bool:
        lSum = 0
        rSum = 0
        lQ = 0
        rQ = 0

        n = len(num)
        mid = n // 2

        for i in range(n):
            if i < mid:
                if num[i] != '?':
                    lSum += int(num[i])
                else:
                    lQ += 1
            else:
                if num[i] != '?':
                    rSum += int(num[i])
                else:
                    rQ += 1

        # No '?' left
        if lQ == 0 and rQ == 0:
            return lSum != rSum

        # Same number of '?' on both sides
        if lQ == rQ:
            return lSum != rSum

        # Difference in number of '?'
        qDiff = abs(lQ - rQ)

        # Odd number of unmatched '?' -> Alice gets the decisive move
        if qDiff % 2 == 1:
            return True

        # If extra '?' are on the left
        if lQ > rQ:
            # Left already has the larger sum -> Alice wins
            if lSum > rSum:
                return True

            # Left has smaller sum. Bob can win only if
            # he can exactly compensate the difference.
            return lSum + (qDiff // 2) * 9 != rSum

        # Extra '?' are on the right
        else:
            # Right already has the larger sum -> Alice wins
            if rSum > lSum:
                return True

            # Right has smaller sum
            return rSum + (qDiff // 2) * 9 != lSum