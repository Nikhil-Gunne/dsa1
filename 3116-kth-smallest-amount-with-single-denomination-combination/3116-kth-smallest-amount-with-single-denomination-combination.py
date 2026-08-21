class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        # product of 2 numbers = lcm(a,b) * gcd(a,b)
        def getLcm(a,b):
            return (a*b)//gcd(a,b)

        def count(x):
            c = 0
            for mask in range(1,(1<<n)):
                #lcm for removing overlapping counts

                # x is 12 
                # 2-> 2 4 6 8 10 12
                # 4-> 4 8 12 
                # cnt = 9 but there are repeated values to remove them take the lcm of 2 numbers and divide x by the lcm will remove the count added multiple times
                currLcm = 1
                bitCnt = 0
                for j in range(n):
                    if mask & (1<<j):
                        bitCnt += 1
                        currLcm = getLcm(currLcm,coins[j])
                
                if bitCnt % 2 == 1:
                    c += x//currLcm
                else:
                    c-=x//currLcm
            return c
    

        low = 1
        high = 25 * 2 * 10**9
        res = -1
        while low <= high:
            mid = low + (high-low)//2
            if count(mid) < k:
                low = mid + 1
            else:
                res = mid
                high = mid - 1
        return res