class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        pref = []
        curr = 0
        for i in stoneValue:
            curr += i
            pref.append(curr)
        
        def getPrefixSum(s,e):
            if s==0:
                return pref[e]
            return pref[e]-pref[s-1]
        
        dp = {}

        def solve(s,e):
            # print(s,e)
            if s>=e:
                return 0
            
            if (s,e) in dp:
                return dp[(s,e)]
            res = 0
            for i in range(s,e):
                leftHalf = getPrefixSum(s,i)
                rightHalf =  getPrefixSum(i+1,e)
                # print(i,leftHalf,rightHalf)
                if leftHalf < rightHalf:
                    if res >= 2*leftHalf:
                        continue
                    res= max(res,leftHalf+solve(s,i))
                elif leftHalf > rightHalf:
                    if res>=2*rightHalf:
                        break
                    res = max(res,rightHalf+solve(i+1,e))
                else:
                    res= max(res,leftHalf+solve(s,i))
                    res = max(res,rightHalf+solve(i+1,e))
            dp[(s,e)] = res
            return res
        
        return solve(0,n-1)



        