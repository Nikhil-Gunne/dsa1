class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp= set(nums)
        mx =0

        for i in mp:
            if i-1 not in mp:
                temp=i
                cnt = 0
                while temp in mp:
                    temp+=1
                    cnt+=1
                mx= max(cnt,mx)
        return mx