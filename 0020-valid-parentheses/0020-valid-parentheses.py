class Solution:
    def isValid(self, s: str) -> bool:

        st = []

        for i in s:
            if i in '[{(':
                st.append(i)
            else:
                if i == ']' and st and st[-1] == '[':
                    st.pop()
                elif i == '}' and st and st[-1] == '{':
                    st.pop()
                    
                elif i == ')' and st and st[-1] == '(':
                    st.pop()
                else:
                    return False
            
        return True if len(st) == 0 else False
        