class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # F[K] = 0.A0 + 1.A1 + 2*A2 + 3*A3 + ... +N-1 * AN-1 
        #F[K+1] = 1.A0 + 2.A1 + 3 * A2 + 4 * A3 + ... + 0 AN-1
        # F[K+1] - F[K] = A0 + A1 + A2 + A3 + ... - (N-1) * AN-1
        # F[K+1] - F[K] = A0 + A1 + A2 + A3 + ... - (N* AN-1 - 1 *AN-1)
        # F[K+1] - F[K] = A0 + A1 + A2 + A3 + ... - N* AN-1 + 1 *AN-1)
        # F[K+1] - F[K] = A0 + A1 + A2 + A3 + ...1 *AN-1 - N* AN-1 
        # F[K+1]  = F[K] +A0 + A1 + A2 + A3 + ...1 *AN-1 - N* AN-1 
        # F(k+1) = F(k) + Sum - (n * nums[n - 1 - k])
        totSum = 0
        sm = 0
        n = len(nums)
        for i in range(n):
            totSum += nums[i]
            sm += (i *nums[i])
        res = float('-inf')
        for i in range(n):
            temp = sm + totSum - (n * nums[n-i-1])
            res = max(temp,res)
            sm = temp
            
        return res
        

        
        
            