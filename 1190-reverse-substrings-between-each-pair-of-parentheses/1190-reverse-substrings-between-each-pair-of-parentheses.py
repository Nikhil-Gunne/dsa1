class Solution:
    def reverseParentheses(self, s: str) -> str:
        

        st = []
        curr = ""
        #whenever open bracket is encountered push the current string to stack and empty the current string 
        #whenever closing bracket is encountered reverse the current string and pop the previous string from stack and concatenate both
        #whenever a character is encountered add it to current string
        for i in s:
            if i == '(':
                st.append(curr)
                curr = ""
            elif i == ')':
                curr = st.pop() + curr[::-1]
            else:
                curr += i
        
        return curr