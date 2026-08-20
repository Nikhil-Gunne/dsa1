class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a1 = [nums[0]]
        a2 = [nums[1]]
        for i in nums[2:]:
            if a1[-1] > a2[-1]:
                a1.append(i)
            else:
                a2.append(i)
        return a1 + a2
        