class Solution:
    def smallestPalindrome(self, s: str) -> str:
        curr = ""
        freq = Counter(s)
        charWithOddFreq = ""
        for i in range(26):
            char = chr(97+i)
            if freq[char]:
                if freq[char]%2 == 1:
                    charWithOddFreq = char
                curr += (char*(freq[char]//2))
        
        return curr + charWithOddFreq + curr[::-1] 

        