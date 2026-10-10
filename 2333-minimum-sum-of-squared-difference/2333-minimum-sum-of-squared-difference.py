
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int],k1: int, k2: int) -> int:
        n = len(nums1)
        diffFreq = [0] * (100001)
        req = 0
        for i in range(n):
            diffFreq[abs(nums1[i]-nums2[i])] += 1
            req += abs(nums1[i]-nums2[i])


        ops  = k1 + k2
        if req <= ops:
            return 0
        
        for i in range(100000,0,-1):
            if diffFreq[i]:
                opsReq = min(diffFreq[i],ops)
                diffFreq[i-1] += opsReq
                diffFreq[i] -= opsReq
                ops -= opsReq
        
        res = 0
        for i in range(1,100001):
            res += (diffFreq[i] * (i**2))
        return res

        
