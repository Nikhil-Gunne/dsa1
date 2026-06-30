class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:

        def getSum(word):
            sm = 0
            for ch in word:
                sm+= weights[ord(ch)-97]
            return sm
        

        res = ""
        for word in words:
            sm = getSum(word) % 26
            res += chr(122-sm)
        return res
            
        