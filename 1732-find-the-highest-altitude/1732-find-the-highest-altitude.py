class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        mx = 0
        for i in gain:
            res += i
            mx = max(mx,res)
        return mx

        