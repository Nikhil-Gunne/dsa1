class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = ""
        digitSum = 0
        temp = sum
        for i in range(9,0,-1):
            poss = sum//i
            digitSum += i *poss
            res += str(i) * min(poss,num)
            sum -= i *poss
            num-=poss
            if num <= 0 or sum <= 0:
                break
        
        res += "0" * num
        return res if digitSum == temp else ""

        