class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        cnt = 0
        for i in range(max(101,num1),num2+1):
            wv = 0
            temp =str(i)
            for j in range(1,len(temp)-1):
                if temp[j-1] < temp[j] and temp[j] > temp[j+1]:
                    wv+=1
                elif temp[j-1] > temp[j] and temp[j] < temp[j+1]:
                    wv+=1
            cnt += wv
        return cnt
