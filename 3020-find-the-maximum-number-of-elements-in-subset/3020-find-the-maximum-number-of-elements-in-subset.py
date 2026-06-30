class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums.sort()
        freq = defaultdict(int)
        def getMaxSize(num):
            if num ==1:
                return freq[1]-1 if not freq[1] & 1 else freq[1]
            n = num
            cnt = 0
            while n in freq:
                if freq[n] == 1:
                    return cnt+1
                elif freq[n] >= 2:
                    cnt+=2
                    n *= n
                else:
                    return cnt
            return cnt-1
        
        for i in nums:
            freq[i] += 1
        
        '''
        2 4   16   64 128 256 512 1024
        2 2^2 2^4  2^8 
        '''
        mx = 0
        for i in range(len(nums)):
            if i==0:
                mx = max(mx,getMaxSize(nums[i]) if freq[nums[i]]>=2 else 1)
            elif i>0 and nums[i] != nums[i-1]:
                mx = max(mx,getMaxSize(nums[i]) if freq[nums[i]]>=2 else 1)
        return mx



        
        