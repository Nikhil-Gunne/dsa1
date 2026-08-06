class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        

        temp = n
        while True:
            temp1= 1
            temp2 = temp
            while temp2:
                rem = temp2%10
                temp1 *= rem
                temp2//=10
            
            if temp1 % t == 0:
                return temp
            temp += 1
        
