class Solution:
    def minChanges(self, s: str) -> int:
        # curr = ""
        # count = 0
        # changes = 0
        # for i in range(len(s)):
        #     if count == 0:
        #         count = 1
        #         curr = s[i]
        #     else:
        #         if curr != s[i]:
        #             # print(i,count)
        #             if count % 2 == 0:
        #                 curr = s[i]
        #                 count = 1
        #             else:
        #                 changes += 1
        #                 count = 0
        #         else:
        #             count+=1
        # return changes
        changes = 0

        for i in range(1,len(s),2):
            if s[i] != s[i-1]:
                changes += 1
        return changes


        