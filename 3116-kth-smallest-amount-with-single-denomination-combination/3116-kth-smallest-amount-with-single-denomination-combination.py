class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        if n==1:
            return coins[0]*k

        def getLcm(a,b):
            return (a*b)//gcd(a,b)

        def count(x):
            c = 0
            for i in range(1,(1<<n)):

                currLcm = 1
                bitCnt = 0
                for j in range(n):
                    if i & (1<<j):
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
                print(res)
                high = mid - 1
        return res