class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:


        
        res = float('inf')
        left = 0
        n = len(arr)
        cSum = 0
        best = [float('inf')] * n
        bestMin = float('inf')
        for right in range(n):
            cSum += arr[right]

            while cSum > target:
                cSum -= arr[left]
                left+=1
        
            if cSum == target:
                currLen = right - left + 1
                if left > 0 and best[left-1] != float('inf'):
                    res = min(res,currLen + best[left-1])
                    if res == 2:
                        return res
                bestMin = min(bestMin,currLen)
            best[right] = bestMin

        return res if res != float('inf') else -1

                        
                    





        