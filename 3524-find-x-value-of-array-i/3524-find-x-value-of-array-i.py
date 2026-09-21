class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:


        prevRemCount = [0] * k
        res = [0] * k
        n = len(nums)
        for i in range(n):
            currRemCount = [0] * k
            currEleRem = nums[i] % k
            currRemCount[currEleRem] += 1
            for rem in range(k):
                newRem = (rem * nums[i] ) % k
                currRemCount[newRem] += prevRemCount[rem]
            
            prevRemCount = currRemCount

            for rem in range(k):
                res[rem] += prevRemCount[rem]
        return res

        