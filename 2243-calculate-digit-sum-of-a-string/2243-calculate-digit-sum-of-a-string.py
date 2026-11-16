class Solution:
    def digitSum(self, s: str, k: int) -> str:
        curr = ""
        while len(s) > k:
            for i in range(0,len(s),k):
                curr += str(sum(map(int,s[i:min(len(s),i+k)])))
            s = curr
            curr = ""
        return s
        