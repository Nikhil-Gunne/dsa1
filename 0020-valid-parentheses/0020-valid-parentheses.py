class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if len(stack)==0 or i=='[' or i=='{' or i=='(':
                stack.append(i)
                continue
            else:
                if i==']' and stack[-1]=='[':
                    stack.pop()
                elif i=='}' and stack[-1]=='{':
                    stack.pop()
                elif i==')' and stack[-1]=='(':
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        return False
        

            
            

        