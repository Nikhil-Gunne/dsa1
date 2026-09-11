
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:

        freq = [0] * 10

        for digit in digits:
            freq[digit] += 1

        cnt = 0

        for num in range(100, 1000, 2):
            h, t, o = str(num)
            inth = int(h)
            intt = int(t)
            into = int(o)
            required = [0] * 10
            required[inth] += 1
            required[intt] += 1
            required[into] += 1

            flag = True

            
            if required[inth] > freq[inth] or required[intt] > freq[intt] or required[into] > freq[into]:
                flag = False

            if flag:
                cnt += 1

        return cnt




        

        # res = set()
        # n = len(digits)
        # used = [0] * n

        # def solve(number):
        #     if len(number)==3:
        #         if int(number)%2 == 0 and len(str(int(number))) ==3:
        #             res.add(number)
        #         return 
            
        #     for i in range(n):
        #         if not used[i]:
        #             used[i] = 1
        #             solve(number+str(digits[i]))
        #             used[i] = 0
        # solve('')
        # return len(res)
        