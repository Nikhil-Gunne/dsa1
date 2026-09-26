class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:


        idx = 0
        res = ""
        knowledgeMap = { x[0] : x[1] for x in knowledge}
        n = len(s)
        while idx < n:
            if s[idx] == '(':
                curr = ""
                idx += 1
                while s[idx] != ')':
                    curr+=s[idx]
                    idx+=1
                res += knowledgeMap[curr] if curr in knowledgeMap else "?"
            else:
                res += s[idx]
            idx+=1

        return res
        