from functools import cmp_to_key

class Solution:
    def minSwaps(self, nums: List[int]) -> int:



        def solve(a, b):
            a1,sm1 = a
            b1,sm2 = b
            if sm1 < sm2:
                return -1
            elif sm1 > sm2:
                return 1
            else:
                if a1 > b1:
                    return 1
                elif a1 < b1:
                    return -1
                return 0
        def dSum(n):
            sm = 0
            while n:
                sm += (n%10)
                n//=10
            return sm

        temp = [(num,dSum(num)) for num in nums]
        temp.sort(key=cmp_to_key(solve))
        n = len(temp)
        pos = { nums[i] : i for i in range(n)}
        # print(temp)
        # print(nums)
        swaps = 0
        for i in range(n):
            if temp[i][0] == nums[i]:
                continue
            
            sortedElPos = pos[temp[i][0]]
            pos[nums[i]] = sortedElPos
            pos[nums[sortedElPos]] = i
            nums[i], nums[sortedElPos] = nums[sortedElPos], nums[i]
            swaps += 1
            
        
        
        return swaps