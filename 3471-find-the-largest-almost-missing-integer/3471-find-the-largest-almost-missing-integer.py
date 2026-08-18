class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)

        for i in range(len(nums)-k+1):
            curr = set()
            for j in range(i,i+k):
                if nums[j] not in curr:
                    freq[nums[j]] += 1
                curr.add(nums[j])
        res = -1
        for i in freq:
            if freq[i]==1:
                res=max(res,i)
        return res
        