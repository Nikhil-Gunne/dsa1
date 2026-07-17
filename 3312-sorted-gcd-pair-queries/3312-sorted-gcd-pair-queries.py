class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:

        factors = defaultdict(int)
        mxEl = 0
        for num in nums:
            temp = num
            mxEl = max(num,mxEl)
            for j in range(1,int(sqrt(temp))+1):
                if temp % j ==0:
                    factors[j] += 1
                    if temp//j != j:
                        factors[temp//j] += 1
        # print(factors)
        originalCount = [0] * (mxEl+1)
        temp = sorted(factors.keys(), reverse=True)

        for i in temp:
            originalCount[i] = factors[i] * (factors[i] - 1) // 2
            if originalCount[i] == 0:
                continue
            j = i * 2
            while j <= mxEl:
                originalCount[i] -= originalCount[j]
                j += i
        # print(originalCount)

        for i in range(1,mxEl+1):
            originalCount[i] += originalCount[i-1]
        # print(originalCount)
        def binarySearch(tar):
            low = 0
            high = mxEl
            res  = 0
            while low <= high:
                mid = low + ((high-low)//2)
                if originalCount[mid] >= tar:
                    res = mid 
                    high = mid - 1
                else:
                    low = mid + 1
            return res
        res = []
        for q in queries:
            res.append(binarySearch(q+1))

        return res
        
        
        