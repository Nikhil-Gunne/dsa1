class Solution:
    def totalNumbers(self, digits: List[int]) -> int:

        res = set()
        n = len(digits)
        used = [0] * n

        def solve(number):
            if len(number)==3:
                if int(number)%2 == 0 and len(str(int(number))) ==3:
                    res.add(number)
                return 
            
            for i in range(n):
                if not used[i]:
                    used[i] = 1
                    solve(number+str(digits[i]))
                    used[i] = 0
        solve('')
        return len(res)
        