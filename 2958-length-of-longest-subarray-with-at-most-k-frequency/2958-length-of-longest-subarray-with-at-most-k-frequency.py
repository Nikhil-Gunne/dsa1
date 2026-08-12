class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        freq = SortedList()
        n = len(nums)
        left = 0
        ans = 0
        cnter = defaultdict(int)
        for right in range(n):
            currNum = nums[right]
            if currNum not in cnter:
                freq.add((1,currNum))
                cnter[currNum] +=1
            else:
                pos = bisect_left(freq,(cnter[currNum],currNum))
                cnt,num = freq[pos]
                cnt += 1
                cnter[num] = cnt
                freq.pop(pos)
                freq.add((cnt,num))
            # print(freq)
            while freq and freq[-1][0] > k:
                pos = bisect_left(freq,(cnter[nums[left]],nums[left]))
                cnt,num = freq[pos]
                cnt -= 1
                freq.pop(pos)
                if cnt > 0:
                    cnter[num] = cnt
                    freq.add((cnt,num))
                else:
                    del cnter[num] 
                left+=1
            ans = max(ans,right-left+1)
        return ans




        