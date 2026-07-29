class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        oddChar = ""
        freq = [0] * 26
        for i in s:
            freq[ord(i)-97]+=1
        
        for i in range(26):
            if freq[i] & 1:
                oddChar = chr(97+i)
            
            freq[i] //=2

        # ncr = n!/r!*(n-r)! => n * n-1 * n-2 * n-r+1 * (n-r)!
                                # r! * (n-r)!

        def getCntOfWays(n,r):
            res = 1
            for i in range(1,r+1):
                res = (res * (n-r+i) )// i
                if res >= k:
                    return k
            return res
        res = []
        half = len(s)//2
        for i in range(half):
            for j in range(26):
                if freq[j]:
                    freq[j] -= 1
                    ways = 1
                    letters = sum(freq)
                    # for ii in range(26):
                    #     letters += freq[ii]
                    
                    for ii in range(26):
                        if freq[ii] :
                            ways *= getCntOfWays(letters,freq[ii])
                            letters-= freq[ii]
                            if ways >= k:
                                break
                    
                    if ways >= k:
                        res.append(chr(97+j))
                        break
                    k-=ways
                    freq[j] += 1
        

        if len(res)!=half:
            return ''
        leftHalf = "".join(res)
        return leftHalf + oddChar + leftHalf[::-1] 

        

        