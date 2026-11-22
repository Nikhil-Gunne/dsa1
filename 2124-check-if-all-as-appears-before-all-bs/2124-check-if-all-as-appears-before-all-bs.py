class Solution:
    def checkString(self, s: str) -> bool:
        

        seenB = False
        for i in s:
            if i == 'a' and seenB:
                return False
            if i == 'b':
                seenB = True
        return True