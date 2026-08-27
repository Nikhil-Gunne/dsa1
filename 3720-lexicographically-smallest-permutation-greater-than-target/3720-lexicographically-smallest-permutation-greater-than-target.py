class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        

        freq = [0] * 26
        for i in s:
            freq[ord(i)-97] +=1
        
        self.res = "" 
        
        def solve(idx,curr,greater):
            if idx == len(target):
                if greater:
                    self.res = curr
                    return True
                return False
            
            for i in range(26):
                if freq[i]==0:
                    continue
                char = chr(97+i)
                if not greater and char < target[idx]:
                    continue
                
                isGreater = greater or char > target[idx]
                freq[i]-=1
                if solve(idx+1,curr+char,isGreater):
                    return True
                freq[i]+=1
            return False
        
        solve(0,"",False)
        return self.res



            



        
        
