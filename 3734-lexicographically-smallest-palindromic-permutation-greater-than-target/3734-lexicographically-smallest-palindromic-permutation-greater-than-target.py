class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        

        freq = [0] * 26
        for i in s:
            freq[ord(i)-97] += 1
        
        oddCnt = 0
        oddChar = ""
        for i in range(26):
            if freq[i] == 0:
                continue
            if freq[i] % 2 == 1:
                oddChar = chr(97+i)
                if oddCnt == 1:
                    return ""
                oddCnt += 1
            freq[i]//=2
        
        n=len(s)

        self.res = ""
        def solve(idx,curr,greater):
            if idx ==(n//2):
                temp = curr + oddChar + curr[::-1]
                if temp > target:
                    self.res = temp
                    return True
                return False
            
            for i in range(26):
                if freq[i] == 0:
                    continue
                char = chr(97+i)
                if not greater and char < target[idx]:
                    continue

                isGreater = greater or char > target[idx]
                freq[i]-=1
                if solve(idx+1,curr+char,isGreater):
                    return True
                freq[i] += 1
            return False
         


        solve(0,"",False)
        return self.res 
            
