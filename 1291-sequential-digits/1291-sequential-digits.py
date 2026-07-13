class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        q = deque([i for i in range(1,10)])
        res = []
        while q:
            curr = q.popleft()

            # print(q)
            if low<=curr and curr<=high:
                res.append(curr)
            
            lastDigit = curr % 10
            if lastDigit <9:
                newNum = (curr*10) + (lastDigit+1)
                if newNum <=high :
                    q.append(newNum)
        return res
